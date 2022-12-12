import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Steam")

# Create a label for the user's name
user_label = tk.Label(root, text="User Name")
user_label.pack()

# Create a text entry field for the user's name
user_entry = tk.Entry(root)
user_entry.pack()

# Create a label for the user's steam id
steam_label = tk.Label(root, text="Steam ID")
steam_label.pack()

# Create a text entry field for the user's steam id
steam_entry = tk.Entry(root)
steam_entry.pack()

# Create a button for submitting the user's data
submit_button = tk.Button(root, text="Submit")
submit_button.pack()

# Start the main event loop
root.mainloop()