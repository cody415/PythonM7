import tkinter as tk
from datetime import date

# Function to calculate age
def calculate_age():
    try:
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())

        dob = date(year, month, day)
        today = date.today()

        # Calculate age
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        result_label.config(text=f"Your Age: {age} years")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")

# Create main window
root = tk.Tk()
root.title("Age Calculator")

# Labels and entry fields
tk.Label(root, text="Enter Day of Birth:").pack(pady=5)
entry_day = tk.Entry(root)
entry_day.pack(pady=5)

tk.Label(root, text="Enter Month of Birth:").pack(pady=5)
entry_month = tk.Entry(root)
entry_month.pack(pady=5)

tk.Label(root, text="Enter Year of Birth:").pack(pady=5)
entry_year = tk.Entry(root)
entry_year.pack(pady=5)

# Button to calculate age
calc_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calc_button.pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="Your Age: ")
result_label.pack(pady=10)

# Run the application
root.mainloop()
