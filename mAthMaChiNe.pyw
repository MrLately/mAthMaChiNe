import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("mAthMaChiNe")  # Set the title of the window
root.geometry("275x75")

filename = ""  # Global variable to store the name of the file

def calculate_income():
    # Read the income data from the file
    with open(filename, "r") as f:
        income_data = f.read()

    # Initialize a variable to store the total income
    total_income = 0

    # Split the income data into separate lines
    lines = income_data.split("\n")

    # Iterate through each line of income data
    for line in lines:
        # Split the line into words
        words = line.split()

        # Iterate through each word in the line
        for word in words:
            # If the word contains a "$" sign, extract the amount and add it to the total income
            if "$" in word:
                amount = float(word.replace("$", "").replace(",", ""))
                total_income += amount

    # Update the text of the label widget with the total income
    total_income_label.config(text=f"Total income: ${total_income:.2f}")

def browse_file():
    global filename
    # Open a file browser and allow the user to select a file
    filename = filedialog.askopenfilename()

# Create the Calculate and Browse buttons
calculate_button = tk.Button(root, text="Calculate", command=calculate_income)
browse_button = tk.Button(root, text="Browse", command=browse_file)

# Create a label widget to display the total income
total_income_label = tk.Label(root, text="")

# Add the buttons and the label to the window
calculate_button.pack()
browse_button.pack()
total_income_label.pack()

# Run the main loop of the tkinter window
root.mainloop()



