# Name: Colin Eade
# Date: November 29, 2022
# App Name: Caesar Cipher
# Description: App that encrypts and decrypts secret messages using the Caesar Cipher

from tkinter import *           # Makes GUI apps
from tkinter.ttk import *       # Replace W95 look
from tkinter import messagebox  # Pop-up message 

# Constants
ENCRYPTION_KEY = 15             # The key for the encrypt and decrypt functions
ENCRYPT_VALUE  = 1              # Value store for encrypt radio button
DECRYPT_VALUE  = 2              # Value store for decrypt radio button

# Functions
def encrypt(message):
    """Encrypts a message when called upon"""

    encrypted_message = ""                                              # Start with an empty string for the new encrypted message

    for character in message:                                           # Go through every character in the message passed through the function
        encrypted_message += chr(ord(character) + ENCRYPTION_KEY)       # Each character in the message will shift (where shift amount = ENCRYPTION_KEY) relative to its value in the ASCII table 
    return encrypted_message                                            # Return the new message after all characters have been shifted

def decrypt(message):
    """Decrypts a message when called upon"""

    decrypted_message = ""                                              # Start with an empty string again

    for character in message:                                           # Go through every character in the message passed through the function
        decrypted_message += chr(ord(character) - ENCRYPTION_KEY)       # This is identical to the step in encrypt() but just in reverse
    return decrypted_message                                            # Return the new message after all characters have been shifted
    
def convert_click():
    """Encrypts or decrypts a message when [Convert] is clicked"""

    # Display error if user did not type anything or selects encrypt or decrypt
    if radiobutton_selection.get() == "" or input_text.get() == "":
        messagebox.showerror(title="Error", message="Please write a message and select if you would like to encrypt or decrypt it")
    
    else:
        if radiobutton_selection.get() == ENCRYPT_VALUE:                   # If the radio button is selected on Encrypt
            encrypted_input_text = encrypt(input_text.get())               # Passes the user input text through encrypt()
            output_text.set(encrypted_input_text)                          # The output text will be the encrypted user text
        
        elif radiobutton_selection.get() == DECRYPT_VALUE:                 # If the radio button is selected on Decrypt
            decrypted_input_text = decrypt(input_text.get())               # Passes the user input text through decrypt()
            output_text.set(decrypted_input_text)                          # The output text will be the decrypted user text

def clear_click():
    """Resets the input, output and radio buttons when [Clear] is clicked"""

    input_text.set("")                            # Resets the input text
    output_text.set("")                           # Resets the output text
    radiobutton_selection.set("")                 # Resets the radio buttons

def key_handler(event:Event):
    """Basic keyboard functionality"""

    if event.keysym == "Return":                  # Executes convert_click() when [Enter] is pressed                                                          
        convert_click()
    
    elif event.keysym == "Escape":                # Executes clear_click() when [ESC] is pressed    
        clear_click()

# Setup window
window = Tk()
window.title("Caesar Cipher - Colin Eade")
window.iconbitmap("Caesar.ico")
window.resizable(width=False, height=False)
window.bind("<Key>", key_handler)

# Frames
input_frame   = LabelFrame(text="Enter a message:")
output_frame  = LabelFrame(text="Output:")
buttons_frame = Frame()

# Variables
input_text            = Variable()
output_text           = Variable()
radiobutton_selection = Variable()

# Input Entry
input_entry = Entry(input_frame, width=50, textvariable=input_text)

# Radio buttons
encrypt_radiobutton = Radiobutton(input_frame, text="Encrypt", variable=radiobutton_selection, value=ENCRYPT_VALUE)
decrypt_radiobutton = Radiobutton(input_frame, text="Decrypt", variable=radiobutton_selection, value=DECRYPT_VALUE)

# Output Entry
output_entry = Entry(output_frame, width=50, state="readonly", textvariable=output_text)

# Buttons
convert_button = Button(buttons_frame, text="Convert", command=convert_click)
clear_button   = Button(buttons_frame, text="Clear", command=clear_click)

# App label
app_label = Label(buttons_frame, text="Caesar Cipher", font="Centaur 20")

# Packing the widgets
input_frame.pack(padx=5, pady=5, anchor="w")
input_entry.pack()

encrypt_radiobutton.pack(pady=5, side="left")
decrypt_radiobutton.pack(pady=5)

output_frame.pack(padx=5, anchor="w")
output_entry.pack(pady=(0, 5))

buttons_frame.pack(pady=(0, 5), padx=5, fill="x")
clear_button.pack(side="right")
convert_button.pack(side="right")

app_label.pack(side="left")

# Show the window
window.mainloop()
