import tkinter as tk
import random

# Function to play the game
def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    if choice == computer_choice:
        result = "It's a Tie!"
        color = "blue"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        color = "green"
    else:
        result = "You Lose!"
        color = "red"

    result_label.config(text=f"Your Choice: {choice}\nComputer's Choice: {computer_choice}\nResult: {result}", fg=color)


# Create main window
root = tk.Tk()
root.geometry("400x400")
root.title("Rock Paper Scissors Game")

# Instruction label
instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14))
instruction_label.pack(pady=20)

# Buttons for choices
rock_button = tk.Button(root, text="Rock", width=15, command=lambda: play("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=15, command=lambda: play("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=15, command=lambda: play("Scissors"))
scissors_button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Run the application
root.mainloop()
