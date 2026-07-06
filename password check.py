import tkinter as tk

# Function to check password strength
def check_strength():
    password = entry_password.get()
    length = len(password)

    if length <= 5:
        strength = "Weak"
        color = "red"
    elif 6 <= length <= 8:
        strength = "Medium"
        color = "yellow"
    elif 9 <= length <= 12:
        strength = "Strong"
        color = "lightgreen"
    else:  # length > 12
        strength = "Very Strong"
        color = "darkgreen"

    result_label.config(text=f"Strength: {strength}", fg=color)


# Create main window
root = tk.Tk()
root.geometry("400x400")
root.title("Length Converter App")

# Label and entry for password
label_password = tk.Label(root, text="Enter Password:")
label_password.pack(pady=10)

entry_password = tk.Entry(root, show="*")  # hides input with *
entry_password.pack(pady=10)

# Button to check strength
check_button = tk.Button(root, text="Check Strength", command=check_strength)
check_button.pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="Strength: ", font=("Arial", 14))
result_label.pack(pady=20)

# Run the application
root.mainloop()
