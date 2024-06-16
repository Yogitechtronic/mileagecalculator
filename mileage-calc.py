import tkinter as tk
from tkinter import messagebox

# Define the rates for petrol and diesel
petrol_rate = 104.21
diesel_rate = 88.95

# Create the main window
root = tk.Tk()
root.title("Petrol and Diesel Cost Calculator")

# Create the input fields
distance_label = tk.Label(root, text="Distance (km):")
distance_label.pack()
distance_entry = tk.Entry(root)
distance_entry.pack()

mileage_label = tk.Label(root, text="Mileage (km/l):")
mileage_label.pack()
mileage_entry = tk.Entry(root)
mileage_entry.pack()

# Create the calculate button
def calculate_cost():
    try:
        distance = float(distance_entry.get())
        mileage = float(mileage_entry.get())

        petrol_consumed = distance / mileage
        diesel_consumed = distance / mileage

        petrol_cost = petrol_consumed * petrol_rate
        diesel_cost = diesel_consumed * diesel_rate

        messagebox.showinfo("Results", f"The cost of petrol is ₹{petrol_cost:.2f}\nThe cost of diesel is ₹{diesel_cost:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

calculate_button = tk.Button(root, text="Calculate", command=calculate_cost)
calculate_button.pack()

# Start the main loop
root.mainloop()
