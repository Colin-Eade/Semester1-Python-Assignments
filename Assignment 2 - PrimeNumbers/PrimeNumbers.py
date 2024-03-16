# Name: Colin Eade
# Date: October 29, 2022
# App Name: Prime Numbers
# Description: App that graphically displays all prime numbers up to a user entered limit

# Import system function from os module
from os import system

# Constants
MIN_NUMBER, MAX_NUMBER = 2, 100

# Create an introduction statement
INTRODUCTION = f'''===================
== Prime Numbers ==
===================
'''

# Change the title
system("title Prime Numbers - Colin Eade")

# Print intro
print(INTRODUCTION)

# Contain program in a while loop that allows the user to restart
restart = "r"
while restart == "r":

    # clear terminal on restart
    system("cls")

    # Validation loop for user input
    valid = False
    while not valid:

        # Ask for a number
        user_number = input(f"Enter a number between {MIN_NUMBER} and {MAX_NUMBER}: ")

        # try to convert from string to int
        try:
            user_number = int(user_number)
            numeric = True
        
        except:
            numeric = False
        
        # Error when not numeric
        if numeric == False:
            print("Error - Input must be a whole number.\n")
        
        # Error when not in valid range
        elif user_number < MIN_NUMBER or user_number > MAX_NUMBER:
            print(f"Error - Number must be between {MIN_NUMBER} and {MAX_NUMBER}.\n")

        # Valid input
        else:
            valid = True
        
    # Clear the terminal upon coming to a valid number
    system("cls")

    # Print a formatted banner
    formamtted_banner = f'''============================
== Prime Numbers up to {user_number} ==
============================
'''

    print(formamtted_banner)

    # counter for prime numbers to achieve bonus mark
    prime_number_count = 0

    for prime_number in range (MIN_NUMBER, user_number + 1):    # Check for prime numbers from 2 to the user input
        prime = True                                            # Assume number is prime unless it does not meet parameters below
        for number in range (MIN_NUMBER, prime_number):         # Check each number from 2 up to the possible prime number
            if prime_number % number == 0:                      # If modulus is 0 for any number in the domain, that means that the possible prime number is not valid
                prime = False                                   # If the number isn't valid make false
                break                                           # break the loop if false to avoid unnecessary calculations
        
        if prime == True:                                       # Number is prime if it makes it through the above loop
            prime_number_count += 1                             # Add 1 to the counter for every prime number that is found
            for count in range (0, prime_number):                                  
                print("#", end="")                              # Print hashes on one line that are equal to the prime number               
            print(f" {prime_number}")                           # Print the prime number

    # After all prime numbers within the domain are found, used the tallied counter to print a statement of the amount of primes that were found
    print(f"\nThere are {prime_number_count} prime numbers from {MIN_NUMBER} up to {user_number}")

    # Exit prompt
    input("\nEnter 'r' to restart: ")