# importing tkinter for GUI
import tkinter as tk
from tkinter import messagebox

# importing random module for our game
import random

# initialization
root = tk.Tk()

# Set the geometry of the screen(GUI)
root.geometry("355x70")

# Title
root.title("Rock Paper Scissors")

# computer's choice
a = random.choice(["Rock", "Paper", "Scissor"])


# functions to give the outputs after the button is clicked
def rock():
    if a == "Rock":
        messagebox.showinfo("Results", "computer chose Rock \n Draw")
    elif a == "Paper":
        messagebox.showinfo("Results", "computer chose Paper \n You lose")
    elif a == "Scissor":
        messagebox.showinfo("Results", "computer chose Scissor \n You Win")


def paper():
    if a == "Rock":
        messagebox.showinfo("Results", "computer chose Rock \n You Win")
    elif a == "Paper":
        messagebox.showinfo("Results", "computer chose Paper \n Draw")
    elif a == "Scissor":
        messagebox.showinfo("Results", "computer chose Scissor \n You lost")


def scissor():
    if a == "Rock":
        messagebox.showinfo("Results", "computer chose Rock \n You lost")
    elif a == "Paper":
        messagebox.showinfo("Results", "computer chose Paper \n You Win")
    elif a == "Scissor":
        messagebox.showinfo("Results", "computer chose Scissor \n Draw")


# Making the Buttons
rocks = tk.Button(root, text="Rock", padx=40, pady=20, bg="Black", fg="Blue", command=lambda: rock())
papers = tk.Button(root, text="Paper", padx=40, pady=20, bg="Black", fg="Blue", command=lambda: paper())
scissors = tk.Button(root, text="Scissor", padx=40, pady=20, bg="Black", fg="Blue", command=lambda: scissor())
scissors.grid(row=0, column=3)

# Placing the buttons on the screen
rocks.grid(row=0, column=1)
papers.grid(row=0, column=2)
scissors.grid(row=0, column=3)

root.mainloop()
