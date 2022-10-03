import tkinter as tk
from tkinter import messagebox
import random

window = tk.Tk()

def control():
    global count
    if number1.get().isdigit():
        n1 = int(number1.get())
        count = count + 1
        if n1 > number2:
            text2.configure(text="Less")
        elif n1 < number2:
            text2.configure(text="More")
        else:

            if count == 1:
                text2.configure(text="You found it 1 try", font="Courier 14 bold", justify="center")
                text2.place(x=25, y=130)
            else:
                text2.configure(text="You found it {} tries".format(count), font="Courier 14 bold", justify="center")
                text2.place(x=25, y=130)

    else:
        text2.configure(text="Please enter an integer", font="Courier 14 bold", justify="center")
        text2.place(x=25, y=130)

    number1.selection_range(0, tk.END)


def exit():

    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

window.protocol("WM_DELETE_WINDOW", exit)


window.title("Number Guessing Game")
screenWidth = window.winfo_screenwidth()//2-160
screenHeight = window.winfo_screenheight()//2-100
window.geometry("320x200+{}+{}".format(screenWidth, screenHeight))


text1 = tk.Label(window, text="Enter numbers from 1-10", font= "Courier 14 bold", width=25, justify="center")
text1.place(x=20, y=15)

number1 = tk.Entry(window, font="Courier 14 bold", width=15, justify="center")
number1.place(x=80, y=50)

controlButton = tk.Button(window, text="Check", font="Courier 14 bold", width=10, command=control)
controlButton.place(x=100, y=85)

text2 = tk.Label(window, text="", font="Courier 16 bold", width=25, justify="center")
text2.place(x=-5, y=130)

author = tk.Label(window, text="This game was made by Ridvan KARASUBAŞI in 2022.", font="Courier 6 bold", width=50, justify="center")
author.place(x=-5, y=180)

number2 = random.randint(1, 9)
count = 0

window.mainloop()