from lib.recipe import Recipe

"""
Recipe constructs with an id, title, ingredients, allergens, prep_time, cook_time, meal_type, appliances and book_id
"""
def test_recipe_constructs():
    recipe = Recipe(1, "Test Title", "Test Ingredients", "Test Allergens", 15, 30, "Main course", "Oven", 3)
    assert recipe.id == 1
    assert recipe.title == "Test Title"
    assert recipe.ingredients == "Test Ingredients"
    assert recipe.allergens == "Test Allergens"
    assert recipe.prep_time == 15
    assert recipe.cook_time == 30
    assert recipe.meal_type == "Main course"
    assert recipe.appliances == "Oven"
    assert recipe.book_id == 3



"""
Recipes format to strings nicely
"""
def test_recipes_format_nicely():
    recipe = Recipe(1, "Test Title", "Test Ingredients", "Test Allergens", 15, 30, "Main course", "Oven", 3)
    assert str(recipe) == "Recipe(1, Test Title, Test Ingredients, Test Allergens, 15, 30, Main course, Oven, 3)"


"""
When two identical recipes are compared, they are equal
"""
def test_recipes_are_equal():
    recipe1 = Recipe(1, "Test Title", "Test Ingredients", "Test Allergens", 15, 30, "Main course", "Oven", 3)
    recipe2 = Recipe(1, "Test Title", "Test Ingredients", "Test Allergens", 15, 30, "Main course", "Oven", 3)
    assert recipe1 == recipe2
