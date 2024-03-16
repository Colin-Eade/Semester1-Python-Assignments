# Name: Colin Eade
# App name: HST Calculator
# Date: November 21, 2022
# Description: Show a dollar amount with added HST

from tkinter import * # Import the tkinter module
from tkinter.ttk import * # Replace the W95 look with a modern one

# Constants
HST = 1.13 # Add 13%

# Define functions - just below the imports
def calculate_click():
    """Executed when the calculate button is clicked"""
    # Get the dollar amount from the input entry
    dollar_amout = input_text.get()

    # Remove $ from dollar amount
    dollar_amout = dollar_amout.replace("$", "")

    # Try to convert to float
    try:
        dollar_amout = float(dollar_amout)
        numeric = True
    except:
        numeric = False

    # Error incase not numeric
    if not numeric or dollar_amout < 0:
        # Display the error in the output entry
        output_text.set("Error - Input is not valid!")

    # It's numeric
    else:
        # Add 13% to the dollar amount
        result = dollar_amout * HST

        # Display the result
        output_text.set(f"${result:.2f}")
        input_text.set(f"${dollar_amout:.2f}")

def clear_click():
    """Reset both input and output to $0.00"""
    output_text.set("$0.00")
    input_text.set("$0.00")

def key_handler(event:Event):
    """Handle key presses"""
    if event.keysym == "Return": # enter key
        calculate_click()
    
    elif event.keysym == "Escape":
        clear_click()

# Setup the window
window = Tk()                               # Create a window 
window.title("HST Calculator - Colin Eade") # Change the title
window.iconbitmap("MoneyBag.ico")           # Change the window icon
window.resizable(width=False, height=False) # Not resizable
window.bind("<Key>", key_handler) # K is uppercase

# Frame - holds all the other widgets
frame = Frame()

# Create Labels
input_label = Label(frame, text="Enter a dollar amount:")
output_label = Label(frame, text="Amount + HST:")

# Variables
input_text  = Variable()
output_text = Variable()
# Set the default values
input_text.set("$0.00")
output_text.set("$0.00")

# Create Entries
input_entry  = Entry(frame, width=50, textvariable=input_text)
output_entry = Entry(frame, width=50, state="readonly", cursor="no", textvariable=output_text)

# Create the buttons
calculate_button = Button(frame, text="Calculate", command=calculate_click)
clear_button     = Button(frame, text="Clear", command=clear_click)

# Place widgets in the window
frame.pack(padx=10, pady=10)        # 10px padding around the frame
input_label.pack(anchor="w")        # Move the text to the left
input_entry.pack(pady=(0,10))       # Padding at the bottom
output_label.pack(anchor="w")       # Move the text to the left
output_entry.pack(pady=(0,10))      # Padding at the bottom
calculate_button.pack(side="right") # Place on the right side
clear_button.pack(side="left")      # Place on the left side


# Make the window visible
window.mainloop()