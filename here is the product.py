import tkinter as tk

# Function to calculate product
def calculate_product():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    except ValueError:
        result_label.config(text="Please enter valid integers!")

# Create main window
root = tk.Tk()
root.title("Multiply Two Numbers")

# Labels and entry fields
label1 = tk.Label(root, text="Enter first number:")
label1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

label2 = tk.Label(root, text="Enter second number:")
label2.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Button to calculate
calc_button = tk.Button(root, text="Calculate Product", command=calculate_product)
calc_button.pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="Product: ")
result_label.pack(pady=10)

# Run the application
root.mainloop()
