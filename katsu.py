print("Welcome to Katsu Curry Kingdom!")

size = input("What size of Katsu Curry would you like? (Small/Medium/Large): ")
print(f"You chose a {size} Katsu Curry.")

extras = input("Any extra ingredients?: ")
print(f"Adding the following extras: {extras}")

meal = input("Would you like to make it a meal? (yes/no): ")
if meal.lower() == "yes":
    side = input("Choose a side (Edamame, Vegetable Tempura, Miso Tofu): ")
    drink = input("Choose a drink (Soda, Juice, Water, Tea): ")
    print(f"Meal selected with {side} and {drink}.")
else:
    print("No meal selected.")

print("Enjoy your custom katsu curry from Katsu Curry Kingdom! Come again soon!")
