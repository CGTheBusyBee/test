# print("In the mystical lands of Pythondale, you've come across a magic potion shop. The shop has a list of potions, and each potion has a set number of ingredients. Your goal is to buy all the ingredients for a specific potion, one ingredient at a time until you have them all.")
      

# ASSIGNMENT 6
# Display a list of potions for the user to choose from.
# Ask the user to choose a potion.
# Display the ingredients required for that potion.
# Use a loop to "buy" each ingredient one by one until all ingredients 
# have been purchased.

# Dictionary containing potions and their ingredients
potions = { 
    "Invisibility Potion": ["Dragon scale", "Fairy dust", "Moonstone"],
    "Flying Potion": ["Phoenix feather", "Troll tooth", "Mermaid scale"], 
    "Healing Potion": ["Unicorn horn", "Elf hair", "Golden apple"] }

# Display list of potions

welcome = '''Welcome to the Magic Potion Shop!
Here are the potions we offer:'''
print(welcome)

for potion in potions.keys():
    print(f"{potion}")

# Ask the user to choose a potion.

chosen_potion = input("Which potion would you like to buy ingredients for? ").strip().title()
chosen_potion_name = chosen_potion
chosen_potion_ingredients = potions[chosen_potion_name]

print(f"\nThe ingredients for {chosen_potion_name} are: ")
for ingredient in chosen_potion_ingredients:
    print(f"{ingredient}")
print("\nLet's start buying the ingredients!")
# Use a while loop to 'buy' each ingredient one by one
purchased_ingredients = []
while len(purchased_ingredients) < len(chosen_potion_ingredients):
    next_ingredient = chosen_potion_ingredients[len(purchased_ingredients)]
    buy_choice = input(f"Do you want to buy {next_ingredient}? (yes/no): ").strip().lower()
    
    if buy_choice == 'yes':
        purchased_ingredients.append(next_ingredient)
        print(f"You bought {next_ingredient}!")
    else:
        print("You chose to stop shopping.")
        break

# check to see if all ingredients were bought
if len(purchased_ingredients) == len(chosen_potion_ingredients):
    print(f"\nCongratulations! you bought all the ingredients for {chosen_potion_name}!")
else:
    print(f"\nYou did not purchase all the ingredients for {chosen_potion_name}. ")





# The syntax for enumerate is: enumerate (iterable, start=0).

# Enumerate is a built-in function in python that allows you to keep 
# track of the number of iterations (loops) in a loop. This enumerate 
# object contains a count (from the start, which always defaults to 0) 
# and a value obtained from iterating over the iterable object