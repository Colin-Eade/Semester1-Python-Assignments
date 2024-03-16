# Name: Colin Eade
# Date: December 10, 2022
# App Name: Temperature Conversion
# Description: App that converts Celsius, Fahrenheit, and Kelvin temperatures to each other

from tkinter import *           # Makes GUI apps
from tkinter.ttk import *       # Replace W95 look

# Constants
TEMPERATURE_UNITS  = ["Celsius", "Fahrenheit", "Kelvin"]            # These will appear as selections in the comboboxes
INPUT_TEXT_DEFAULT = 32                                             # The default value for the input text upon launching or clearing the app

# Functions
# First 6 are very straight forward conversion formulas
def celsius_to_fahrenheit(temperature):
    """Celsius to Fahrenheit conversion"""
    conversion = (temperature * (9/5)) + 32
    return conversion

def celsius_to_kelvin(temperature):
    """Celsius to Kelvin conversion"""
    conversion = temperature + 273.15
    return conversion

def fahrenheit_to_celsius(temperature):
    """Fahrenheit to Celsius conversion"""
    conversion = (temperature - 32) * (5/9)
    return conversion

def fahrenheit_to_kelvin(temperature):
    """Fahrenheit to Kelvin conversion"""
    conversion = (temperature - 32) * (5/9) + 273.15
    return conversion

def kelvin_to_celsius(temperature):
    """Kelvin to Celsius conversion"""
    conversion = temperature - 273.15
    return conversion

def kelvin_to_fahrenheit(temperature):
    """Kelvin to Fahrenheit conversion"""
    conversion = (temperature - 273.15) * (9/5) + 32
    return conversion

def convert_click():
    """Converts the user input to their desired result when [Convert] is clicked"""
    try:
        temperature = float(input_text.get())                                       # try to turn the user input into a floating point so we can output decimal values
    except:             
        output_text.set("ERROR - Enter a number")                                   # if the user does not enter a number it will not accept the input. This includes leaving the input blank or inputting text. 
        return                                                                      #       - Outputs into the output entry as instructed

    if input_selection.get() == output_selection.get():                             # if the combobox selections are the same then there is no conversion and input = output
        temperature = temperature
    
    elif input_selection.get() == TEMPERATURE_UNITS[0] and output_selection.get() == TEMPERATURE_UNITS[1]:  # Celsius selection to Fahrenheit selection
        temperature = celsius_to_fahrenheit(temperature)                                                    # execute conversion function
    
    elif input_selection.get() == TEMPERATURE_UNITS[0] and output_selection.get() == TEMPERATURE_UNITS[2]:  # Celsius selection to Kelvin selection
         temperature = celsius_to_kelvin(temperature)                                                       # execute conversion function
    
    elif input_selection.get() == TEMPERATURE_UNITS[1] and output_selection.get() == TEMPERATURE_UNITS[0]:  # Fahrenheit selection to Celsius selection
        temperature = fahrenheit_to_celsius(temperature)                                                    # execute conversion function
    
    elif input_selection.get() == TEMPERATURE_UNITS[1] and output_selection.get() == TEMPERATURE_UNITS[2]:  # Fahrenheit selection to Kelvin selection
        temperature = fahrenheit_to_kelvin(temperature)                                                     # execute conversion function
    
    elif input_selection.get() == TEMPERATURE_UNITS[2] and output_selection.get() == TEMPERATURE_UNITS[0]:  # Kelvin selection to Celsius selection
        temperature = kelvin_to_celsius(temperature)                                                        # execute conversion function
    
    elif input_selection.get() == TEMPERATURE_UNITS[2] and output_selection.get() == TEMPERATURE_UNITS[1]:  # Kelvin selection to Fahrenheit selection
        temperature = kelvin_to_fahrenheit(temperature)                                                     # execute conversion function
    
    temperature = round(temperature, 1)                                                                     # Round the value to 1 decimal place
    output_text.set(temperature)                                                                            # set the output text to the value

def clear_click():
    """Resets the input, output and comboboxes to their defaults when [Clear] is clicked"""
    input_text.set(INPUT_TEXT_DEFAULT)                              # Resets the input text to 32                                 
    output_text.set(fahrenheit_to_celsius(input_text.get()))        # Resets the output text to the Fahrenheit to Celsius conversion of the input text
    input_selection.set(TEMPERATURE_UNITS[1])                       # Resets the input combobox unit to a default of Fahrenheit
    output_selection.set(TEMPERATURE_UNITS[0])                      # Resets the input combobox unit to a default of Celsius   
                                                                    #           - These commands make the default display a calculation example as instructed
def key_handler(event:Event):
    """Basic keyboard functionality"""
    if event.keysym == "Return":                        # Executes convert_click() when [Enter] is pressed
        convert_click()
    
    elif event.keysym == "Escape":                      # Executes clear_click() when [ESC] is pressed              
        clear_click()

# Setup window
window = Tk()
window.title("Temperature Conversion - Colin Eade")
window.iconbitmap("Temperature.ico")
window.resizable(width=False, height=False)
window.bind("<Key>", key_handler)


# Frames
conversion_frame = LabelFrame(text="Temperature Conversion")
input_cb_frame   = LabelFrame(text="From:")
output_cb_frame  = LabelFrame(text="To:")
buttons_frame    = Frame()

# Variables
input_text          = Variable()
output_text         = Variable()
input_selection     = Variable()
output_selection    = Variable()

# Input Entry
input_text.set(INPUT_TEXT_DEFAULT)      # Defaults input text to 32         - For instructed default
input_entry = Entry(conversion_frame, justify="center", width=26, textvariable=input_text)

# Equal sign
output_text.set(fahrenheit_to_celsius(input_text.get()))    # Defaults the output text to the Fahrenheit to Celsius conversion of the input text default        - For instructed default
equal_sign_label = Label(conversion_frame, text="=", font="Calibri 20")

# Output Entry
output_entry = Entry(conversion_frame, justify="center", width=26, state="readonly", textvariable=output_text)

# Input Combobox
input_selection.set(TEMPERATURE_UNITS[1])           # Defaults input combobox to Fahrenheit         - For instructed default
input_combobox = Combobox(input_cb_frame, width=23, values=TEMPERATURE_UNITS, textvariable=input_selection, state="readonly")

# Output Combobox
output_selection.set(TEMPERATURE_UNITS[0])          # Defaults output combobox to Celsius           - For instructed default
output_combobox = Combobox(output_cb_frame, width=23,  values=TEMPERATURE_UNITS, textvariable=output_selection, state="readonly")

# Buttons
convert_button = Button(buttons_frame, text="Convert", command=convert_click)
clear_button   = Button(buttons_frame, text="Clear", command=clear_click)

# Packing the widgets
conversion_frame.pack(fill="x", padx=5, pady=5)
input_entry.pack(side="left", padx=(5,0))
equal_sign_label.pack(side="left", padx=5)
output_entry.pack(side="left",padx=(0,5))

input_cb_frame.pack(fill="x", side="left",anchor="n", padx=(5,15), pady=(0,5))
input_combobox.pack(anchor="w", padx=(5,5))

output_cb_frame.pack(fill="x", expand=True, anchor="n", padx=(0,5))
output_combobox.pack(anchor="w", padx=5)

buttons_frame.pack(side="right", anchor="w",padx=(0,15), pady=5)
convert_button.pack(side="left")
clear_button.pack(side="right")

# Show the window
window.mainloop()