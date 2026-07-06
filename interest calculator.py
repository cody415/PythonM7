import tkinter as tk

# Function to calculate interests
def calculate_interest():
    try:
        # Get values from entry fields
        principal = float(entry_principal.get())
        time = float(entry_time.get())
        rate = float(entry_rate.get())

        # Simple Interest formula: (P * T * R) / 100
        simple_interest = (principal * time * rate) / 100

        # Compound Interest formula: P * (1 + R/100)^T - P
        compound_interest = principal * ((1 + rate / 100) ** time) - principal

        # Display results
        result_label.config(
            text=f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest:.2f}"
        )
    except ValueError:
        result_label.config(text="Please enter valid numbers!")


# Create main window
root = tk.Tk()
root.title("Interest Calculator")

# Labels and entry fields
tk.Label(root, text="Enter Principal Amount:").pack(pady=5)
entry_principal = tk.Entry(root)
entry_principal.pack(pady=5)

tk.Label(root, text="Enter Time Period (years):").pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack(pady=5)

tk.Label(root, text="Enter Rate of Interest (%):").pack(pady=5)
entry_rate = tk.Entry(root)
entry_rate.pack(pady=5)

# Button to calculate
calc_button = tk.Button(root, text="Calculate Interest", command=calculate_interest)
calc_button.pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="Simple Interest: \nCompound Interest: ")
result_label.pack(pady=10)

# Run the application
root.mainloop()
