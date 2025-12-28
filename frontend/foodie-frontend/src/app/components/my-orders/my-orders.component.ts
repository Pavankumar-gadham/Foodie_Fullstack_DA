import { Component, OnInit } from '@angular/core';
import { RecipeService } from 'src/app/services/recipe.service';
import { PurchasedRecipe } from 'src/app/purchased-recipe.model';

@Component({
  selector: 'app-my-orders',
  templateUrl: './my-orders.component.html',
  styleUrls: ['./my-orders.component.css']
})
export class MyOrdersComponent implements OnInit {

  purchasedRecipes: PurchasedRecipe[] = []; // ✅ FIX

  constructor(private recipeService: RecipeService) {}

  ngOnInit(): void {
    this.recipeService.getPurchasedRecipes().subscribe({
      next: data => this.purchasedRecipes = data,
      error: err => console.error(err)
    });
  }
}
