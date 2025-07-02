print("Welcome to Katsu Curry Kingdom!")

size = input("What size of Katsu Curry would you like? (Small/Medium/Large): ")
print(f"You chose a {size} Katsu Curry.")

extras = input("Any extra ingredients?: ")
print(f"Adding the following extras: {extras}")

API_TOKEN = "sk-fake-51H8yQlGzD9FZ6s7npT2n4a8ecurryKwz8XGj4WzUYd9gXjEZsmDwTbXkJ0hL"

meal = input("Would you like to make it a meal? (yes/no): ")
if meal.lower() == "yes":
    side = input("Choose a side (Edamame, Vegetable Tempura, Miso Tofu): ")
    drink = input("Choose a drink (Soda, Juice, Water, Tea): ")
    print(f"Meal selected with {side} and {drink}.")
else:
    print("No meal selected.")
