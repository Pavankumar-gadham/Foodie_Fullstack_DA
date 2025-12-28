import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
from datetime import timedelta
BASE_DIR = Path(__file__).resolve().parent.parent
# ======================
# LOAD ENVIRONMENT FILE
# ======================
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")
if ENVIRONMENT == "production":
 load_dotenv(BASE_DIR / ".env.prod")
else:
 load_dotenv(BASE_DIR / ".env.local")
# ======================
# DJANGO CORE
# ======================
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
DEBUG = os.getenv("DJANGO_DEBUG") == "True"
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",")
# ======================
# APPLICATIONS
# ======================
INSTALLED_APPS = [
 "django.contrib.admin",
 "django.contrib.auth",
 "django.contrib.contenttypes",
 "django.contrib.sessions",
 "django.contrib.messages",
 "django.contrib.staticfiles",
 "corsheaders",
 "rest_framework",
 "rest_framework_simplejwt",
 "recipes",
 "django_celery_results"
]
# ======================
# MIDDLEWARE
# ======================
MIDDLEWARE = [
 "corsheaders.middleware.CorsMiddleware",
 "django.middleware.security.SecurityMiddleware",
 "whitenoise.middleware.WhiteNoiseMiddleware",
 "django.contrib.sessions.middleware.SessionMiddleware",
 "django.middleware.common.CommonMiddleware",
 "django.middleware.csrf.CsrfViewMiddleware",
 "django.contrib.auth.middleware.AuthenticationMiddleware",
 "django.contrib.messages.middleware.MessageMiddleware",
 "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "foodie_haven.urls"
WSGI_APPLICATION = "foodie_haven.wsgi.application"
# ======================
# TEMPLATES
# ======================
TEMPLATES = [
 {
 "BACKEND": "django.template.backends.django.DjangoTemplates",
 "DIRS": [BASE_DIR / "templates"],
 "APP_DIRS": True,
 "OPTIONS": {
 "context_processors": [
 "django.template.context_processors.debug",
 "django.template.context_processors.request",
 "django.contrib.auth.context_processors.auth",
 "django.contrib.messages.context_processors.messages",
 ],
 },
 },
]
# ======================
# DATABASE
# ======================
DATABASES = {
 "default": {
 "ENGINE": "django.db.backends.mysql",
 "NAME": os.getenv("DB_NAME"),
 "USER": os.getenv("DB_USER"),
 "PASSWORD": os.getenv("DB_PASSWORD"),
 "HOST": os.getenv("DB_HOST"),
 "PORT": os.getenv("DB_PORT"),
 }
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# ======================
# STATIC & MEDIA
# ======================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
# ======================
# SECURITY
# ======================
if not DEBUG:
 SECURE_SSL_REDIRECT = True
 CSRF_COOKIE_SECURE = True
 SESSION_COOKIE_SECURE = True
# ======================
# CORS / CSRF
# ======================
CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "").split(",")
CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")
# ======================
# JWT
# ======================
SIMPLE_JWT = {
 "ACCESS_TOKEN_LIFETIME": timedelta(minutes=int(os.getenv("JWT_ACCESS_TOKEN_MINUTES", 60))),
 "REFRESH_TOKEN_LIFETIME": timedelta(days=int(os.getenv("JWT_REFRESH_TOKEN_DAYS", 7))),
}
# ======================
# REDIS / CELERY
# ======================
# Redis / Celery
REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")

CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = REDIS_URL

# Cache
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# ======================
# EMAIL
# ======================
EMAIL_BACKEND = os.getenv(
 "EMAIL_BACKEND",
 "django.core.mail.backends.smtp.EmailBackend"
)
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True") == "True"
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# ======================
# RAZORPAY
# ======================
RAZOR_KEY_ID = os.getenv("RAZOR_KEY_ID")
RAZOR_KEY_SECRET = os.getenv("RAZOR_KEY_SECRET")
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CELERY_BROKER_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_BACKEND = "django-db"
CELERY_TIMEZONE = "UTC"
