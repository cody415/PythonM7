import tkinter as tk

# Function to convert inches to centimeters
def convert_length():
    try:
        inches = float(entry_inch.get())
        centimeters = inches * 2.54  # Conversion factor
        result_label.config(text=f"Length in cm: {centimeters:.2f}")
    except ValueError:
        result_label.config(text="Please enter a valid number!")

# Create main window
root = tk.Tk()
root.title("Inches to Centimeters Converter")

# Label and entry for inches
label_inch = tk.Label(root, text="Enter length in inches:")
label_inch.pack(pady=5)

entry_inch = tk.Entry(root)
entry_inch.pack(pady=5)

# Button to convert
convert_button = tk.Button(root, text="Convert", command=convert_length)
convert_button.pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="Length in cm: ")
result_label.pack(pady=10)

# Run the application
root.mainloop()
