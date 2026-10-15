from lib.recipe import *
from lib.recipe_repository import RecipeRepository
from lib.database_connection import DatabaseConnection

def main():
    connection: DatabaseConnection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/recipes.sql")

    repo = RecipeRepository(connection)

    results: list[Recipe] = repo.all()

    for recipe in results:
        print("- " + str(recipe))

if __name__ == "__main__":
    main()