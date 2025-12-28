import { Recipe } from './recipe.model';

export interface PurchasedRecipe {
  id: number;
  recipe: Recipe;
  payment_id: string;
  created_at: string;
}
