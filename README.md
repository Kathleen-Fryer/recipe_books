

# Python Project

This repo  contains the project to assist with choosing recipes for meal planning based on the many books in the house.


> Reminder: If you encounter a `ModuleNotFound` error, deactivate and then reactivate your virtual env.

## Setup

```shell
# Set up the virtual environment
; python -m venv recipe-venv

# Activate the virtual environment
; source recipe-venv/bin/activate 

# Install dependencies
(recipe-venv); pip install -r requirements.txt

# Install the virtual browser we will use for testing
# (makersbnb-venv); playwright install
# If you have problems with the above, contact your coach

# Create a test and development database
(recipe); createdb RECIPE_BOOKS
(recipe-venv); createdb RECIPE_BOOKS_TEST

# Seed the database with the dev Data
(recipe-venv); python seed_dev_database.py 

# Run the tests (with extra logging)
(recipe-venv); pytest -sv

# Run the app
(recipe-venv); python app.py

# Now visit http://localhost:5001/index in your browser
```

## User Stories

When I search for ingredient "chicken" and max_time "30 minutes", I receive a list of recipes that include chicken and take less than 30 minutes overall (prep_time + cooking_time)

When I search author "Mary Berry", I see a list of books by Mary Berry 

When I search meal type "Starter", the page returns a list of books featuring starter recipes and a number of recipes per book

I can add a book to the database and see it in the All list

I can add a recipe to a book and see it in a list of recipes from that book

When I search "milk" in Allergens, I can see a list of recipes with no milk 

/recipe_books shows a list of all books with links to each book

/recipe_books/<book_id> shows author and list of all recipes in each book. Button for add recipe. Links to each recipe

/recipe_books/<book_id>/<recipe_id> shows pre time, cook time, total time, ingredients, allergens, meal type, appliances (oven/hob/air fryer/firdge/freezer)

