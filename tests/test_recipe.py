from lib.recipe import *

def test_recipe_init():
    recipe = Recipe(1, "Salad", 6, 5)

    assert recipe.id == 1
    assert recipe.name == "Salad"
    assert recipe.cooking_time == 6
    assert recipe.rating == 5

def test_recipe_comparison():
    recipe1 = Recipe(1, "Salad", 6, 5)
    recipe2 = Recipe(1, "Salad", 6, 5)
    assert recipe1 == recipe2

def test_recipe_add_string():
    recipe1 = Recipe(1, "Salad", 6, 5)
    assert str(recipe1) == "Recipe(1, 'Salad', 6 , 5)"