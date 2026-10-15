from lib.recipe_repository import *
from lib.recipe import *

def test_get_all(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repo = RecipeRepository(db_connection)
    result = repo.all()
    assert result == [
        Recipe(1, 'Classic Caprese Salad', 10, 3),
        Recipe(2, 'Garlic Butter Shrimp Pasta', 20, 4), 
        Recipe(3, 'Beef and Broccoli Stir-Fry', 25, 5), 
        Recipe(4, 'Chicken Tikka Masala', 45, 5), 
        Recipe(5, 'Classic chocolate chip cookies', 30, 5)
    ]

def test_find(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repo = RecipeRepository(db_connection)
    result = repo.find(1)
    assert result == Recipe(1, 'Classic Caprese Salad', 10, 3)

