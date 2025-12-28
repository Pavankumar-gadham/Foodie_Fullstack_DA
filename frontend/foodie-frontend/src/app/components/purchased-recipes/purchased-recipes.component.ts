import { Component, OnInit } from '@angular/core';
import { RecipeService } from 'src/app/services/recipe.service';
import { Recipe } from 'src/app/recipe.model';
import { PurchasedRecipe } from 'src/app/purchased-recipe.model';

@Component({
  selector: 'app-purchased-recipes',
  templateUrl: './purchased-recipes.component.html',
  styleUrls: ['./purchased-recipes.component.css']
})
export class PurchasedRecipesComponent implements OnInit {
  purchasedRecipes: PurchasedRecipe[] = [];
  showDetails: { [key: number]: boolean } = {};

  constructor(private recipeService: RecipeService) {}

  ngOnInit(): void {
    this.recipeService.getPurchasedRecipes().subscribe({
      next: (recipes) => this.purchasedRecipes = recipes,
      error: (err) => console.error('Failed to load purchased recipes', err)
    });
  }

  toggleDetails(recipeId: number) {
    this.showDetails[recipeId] = !this.showDetails[recipeId];
  }

  getProcessSteps(process?: string): string[] {
  if (!process) {
    return [];
  }
  return process
    .split(/\r?\n/)
    .map(step => step.trim())
    .filter(step => step.length > 0);
}

}
