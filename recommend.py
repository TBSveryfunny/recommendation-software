# Recreation of the example project from
# the Codecademy Portfolio Project prompt, with a comfort feature or two added.

# Import code from other files and required libraries.
import os
import random
import math
from restaurantData import types, restaurant_data
from sort_and_search_types import quicksort, binary_search
from store_and_find_restaurants import HashMap
from restaurant import Restaurant

# Utility exit confirmation and terminal clear functions. 
# These are designed to be compatible with multiple operating systems.

def confirm_exit(msg="Exiting the program. Press any key to confirm."):
  if os.name == 'nt':
    os.system(f"echo {msg} && pause >nul") 
  else:
    os.system(f"read -p {msg}")

def terminal_clear():
  os.system('cls' if os.name == 'nt' else 'clear')

# Sort types using a quicksort algorithm. This is to optimize searches.
quicksort(types)

# Places the elements in a custom HashMap.
restaurants = HashMap(len(types))

# Pops the restaurant data into the HashMap to reduce space complexity.
# Uses the Binary Search function as a hash, and the indexes from that function as hash codes. 
# This is to ensure that the list of elements at a type index can always be retrieved in O(1) time.

while len(restaurant_data) > 0:
  r = restaurant_data.pop()
  restaurants.assign(r[0], Restaurant(r[1:]))

# cake ascii art
cake = '''
                *                
  *             *             *
  *             *             *
  *             *             *
 ***           ***           ***
*****         *****         *****
*********************************
*********************************
*********************************
*********************************
_________________________________
*                               *
*                               *
*  Welcome to SoHo Restaurants! *
*                               *
*_______________________________*'''
terminal_clear()
print(cake)

# function to simplify the process of asking a yes or no question
def yes_to(question):
  inpit = input(question + " Enter 'y' for yes and 'n' for no\n").lower()
  if inpit == 'y':
    return True
  elif inpit == 'n':
    return False
  else:
    print("Sorry, that input was invalid.")
    yes_to(question)

while True:
  # \n is used throughout to create a smooth, visually pleasing look for the program.
  print("\nWhat type of food would you like to eat?")
  print("Type the beginning of that food type and press enter to see if it's here.")
  food = input("").lower()
  if food == "":
    if yes_to("Sorry, no query was entered. Do you want to exit this program?"):
      break
    else:
      continue
  code, tlist = binary_search(types, food)
  tlength = len(tlist)
  if tlength == 0:
    if yes_to("\nSorry, no food types were found for that query. Do you want to exit this program?"):
      break
  elif tlength == 1:
    food = tlist[0].title()
    if yes_to(f"\nThe only option with those beginning letters is {food}. Do you want to look at {food} restaurants?"):
      terminal_clear()
      rlist = restaurants.retrieve(code)
      print(f"The {food} restaurants in SoHo are....", end="")
      print(rlist)
      if not yes_to("\nDo you want to find other restaurants?"):
        break
  else:
    print("\nWith those beginning letters, your choices are " + str(tlist))

confirm_exit()
