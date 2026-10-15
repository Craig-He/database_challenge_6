from lib.database_connection import DatabaseConnection
from lib.recipe import Recipe

class RecipeRepository():
    def __init__(self, connection):
        self._connection: DatabaseConnection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM recipes")
        return [Recipe(row["id"], row["name"], row["cooking_time"], row["rating"]) for row in rows]

    def find(self, id):
        row = self._connection.execute("SELECT * from recipes where id=%s", [id])[0]
        return Recipe(row["id"], row["name"], row["cooking_time"], row["rating"])
        