import tkinter as tk
from tkinter import messagebox

# Function for encryption using Caesar Cipher
def encrypt_message(plain_text, shift):
   encrypted_text = ""
   for char in plain_text:
       if char.isalpha():  # Check if the character is a letter
           shift_base = 65 if char.isupper() else 97  # For uppercase or lowercase letters
           encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
       else:
           encrypted_text += char  # Non-alphabet characters remain unchanged
   return encrypted_text

# Function for decryption using Caesar Cipher
def decrypt_message(encrypted_text, shift):
   decrypted_text = ""
   for char in encrypted_text:
       if char.isalpha():  # Check if the character is a letter
           shift_base = 65 if char.isupper() else 97  # For uppercase or lowercase letters
           decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
       else:
           decrypted_text += char  # Non-alphabet characters remain unchanged
   return decrypted_text

# Function to handle the encryption in the GUI
def handle_encryption():
   plain_text = text_input.get("1.0", "end-1c")  # Get the input text from Text widget
   try:
       shift = int(shift_entry.get())  # Get the shift value from the entry field
       encrypted_text = encrypt_message(plain_text, shift)
       result_text.delete("1.0", "end")  # Clear any previous results
       result_text.insert("1.0", encrypted_text)  # Display encrypted text
   except ValueError:
       messagebox.showerror("Invalid Input", "Please enter a valid shift value.")

# Function to handle the decryption in the GUI
def handle_decryption():
   encrypted_text = text_input.get("1.0", "end-1c")  # Get the input text from Text widget
   try:
       shift = int(shift_entry.get())  # Get the shift value from the entry field
       decrypted_text = decrypt_message(encrypted_text, shift)
       result_text.delete("1.0", "end")  # Clear any previous results
       result_text.insert("1.0", decrypted_text)  # Display decrypted text
   except ValueError:
       messagebox.showerror("Invalid Input", "Please enter a valid shift value.")

# Set up the main Tkinter window
root = tk.Tk()
root.title("Caesar Cipher Encryption/Decryption")

# Create and place the widgets
tk.Label(root, text="Enter your message:").pack(pady=5)

text_input = tk.Text(root, height=5, width=40)  # Text widget for message input
text_input.pack(pady=10)

tk.Label(root, text="Enter shift value (e.g., 3):").pack(pady=5)

shift_entry = tk.Entry(root, width=10)  # Entry widget for shift value
shift_entry.pack(pady=5)

# Buttons for encryption and decryption
encrypt_button = tk.Button(root, text="Encrypt", command=handle_encryption)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=handle_decryption)
decrypt_button.pack(pady=5)

tk.Label(root, text="Result:").pack(pady=5)

result_text = tk.Text(root, height=5, width=40)  # Text widget for displaying result
result_text.pack(pady=10)

# Run the GUI
root.mainloop()
