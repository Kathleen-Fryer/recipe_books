class Recipe:
    def __init__(self, id, title, ingredients, allergens, prep_time, cook_time, meal_type, appliances, book_id):
        self.id = id
        self.title = title
        self.ingredients = ingredients
        self.allergens = allergens
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.meal_type = meal_type
        self.appliances = appliances
        self.book_id = book_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Recipe({self.id}, {self.title}, {self.ingredients}, {self.allergens}, {self.prep_time}, {self. cook_time}, {self.meal_type}, {self.appliances}, {self.book_id})"


