from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from smtplib import SMTPException
from django.utils.timezone import now

@shared_task
def notify_new_recipe(title, description, recipient_email):
    try:
        send_mail(
            'New Recipe Added',
            f'New recipe: {title}\nDescription: {description}',
            settings.DEFAULT_FROM_EMAIL,  
            [recipient_email],           
        )
        return f'Notified {recipient_email} about {title}'

    except (BadHeaderError, SMTPException) as e:
        print(f"Failed to send email to {recipient_email}. Error: {str(e)}")
        return f'Failed to notify {recipient_email} about {title}'
    

@shared_task
def send_subscription_welcome_email(email):
    try:
        send_mail(
            '🎉 Welcome to Foodie Heaven Newsletter!',
            'Thanks for subscribing! Stay tuned for delicious recipes coming your way.',
             settings.DEFAULT_FROM_EMAIL,
            [email],
        )
        return f'Welcome email sent to {email}'
    except (BadHeaderError, SMTPException) as e:
        print(f"❌ Failed to send welcome email to {email}. Error: {str(e)}")
        return f'Failed to notify {email}'


@shared_task
def send_purchase_email(user_email, recipe_title, price, payment_id):
    current_time = now()  # this is already timezone-aware if USE_TZ is True

    subject = f'🧾 Purchase Confirmation - {recipe_title}'
    message = (
        f'Hello,\n\n'
        f'Thank you for your purchase on {current_time.strftime("%A, %d %B %Y")}.\n\n'
        f'🧾 Recipe: {recipe_title}\n'
        f'💰 Price: ₹{price}\n'
        f'🪙 Payment ID: {payment_id}\n\n'
        f'Enjoy your recipe!\n\n'
        f'- Foodie Haven Team'
    )
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user_email],
        fail_silently=False,
    )
