# Name: Colin Eade
# Date: October 5, 2022
# App Name: Pizza Pi
# Description: App that calculates the area of a pizza and the amount of slices it will be cut into

# Import system function from os module
# Import math module
from os import system
import math

# Constants
MIN_DIAMETER, MAX_DIAMETER = 8, 24

# Change the title
system("title Pizza Pi - Colin Eade")

# Ask for pizza diameter
pizza_diameter = input("Please enter the diameter of your pizza: ")

# Try to convert from string to int
try:
    pizza_diameter = int(pizza_diameter)
    valid = True
except:
    valid = False

# Print error if diameter is not numeric or not a whole number
if not valid:
    print("Error - Diameter must be a whole numeric value!")

# Print error if diameter is less than 8 or more than 24
elif pizza_diameter < MIN_DIAMETER or pizza_diameter > MAX_DIAMETER:
    print('Error - Pizza must have a diameter in the range of 8" to 24"!')

# Valid diameter!
else:

    # Set the slice parameters base on the pizza sizes
    if pizza_diameter < 12:
        slices = 6
    
    elif 12 <= pizza_diameter < 14:
        slices = 8
    
    elif 14 <= pizza_diameter < 16:
        slices = 10

    elif 16 <= pizza_diameter < 20:
        slices = 12
    
    else:
        slices = 16

    # Create equations to find the pizza area, slice area, and slice angle and store them as variables
    # Use the round and int functions to round your equations according to the instructions
    pizza_area = round(math.pi*(pizza_diameter/2)**2, 2)
    slice_area = round(pizza_area/slices, 2)
    slice_angle = int(360/slices)

    # Use the variables to create output sentences in formatted strings so the user can see their pizza info
    print(f'A {pizza_diameter}" pizza has an area of {pizza_area} square inches and will yield {slices} slices.')
    print(f'Each slice will be cut at {slice_angle} degrees and have an area of {slice_area} square inches.')

# Exit prompt
input("Press [enter] to exit: ")
