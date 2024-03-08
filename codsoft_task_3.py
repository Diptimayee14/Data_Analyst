import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_display.config(text="Generated Password: " + password)
    except ValueError as ve:
        password_display.config(text="Error: " + str(ve))

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

# Create and pack widgets
length_label = tk.Label(root, text="Enter password length:", font=('Segoe UI', 15, 'bold'))
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=('Segoe UI', 15, 'bold'))
generate_button.pack()

password_display = tk.Label(root, text="")
password_display.pack()

# Run the Tkinter event loop
root.mainloop()
