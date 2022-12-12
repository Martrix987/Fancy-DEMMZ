import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Steam")

# Create a label for the user's name
user_label = tk.Label(root, text="Welkom bij ons project steam!"
                                 " Dit Programma laat zien welke vrienden Online zijn")
user_label.pack()


# Create a label for the user's steam id
steam_label = tk.Label(root, text="Voer hier uw Steam ID in")
steam_label.pack()

# Create a text entry field for the user's steam id
steamID = tk.Entry(root)
steamID.pack()

# Create a button for submitting the user's data
submit_button = tk.Button(root, text="Submit")
submit_button.pack()

# Start the main event loop
root.mainloop()