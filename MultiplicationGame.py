import random
from tkinter import messagebox, simpledialog, Label, ttk
from tkinter import *
import time
import pyttsx3

# module initialization

windows = Tk()
windows.title("Multiplication Quiz")
windows.geometry("300x200")

nex = pyttsx3.init()


def multiply_questions():
    while True:

        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)

        if (num1 >= 11 and num2 >= 11) or (num1 < 11 and num2 < 11):
            continue

        question = f"What is {num1} x {num2}?"
        answer = num1 * num2

        nex.say(question)
        nex.runAndWait()

        # Use a tkinter Entry widget to get user input
        user_input = simpledialog.askstring("Answer", question)

        if user_input is None or user_input.lower() == "exit":
            nex.say("exiting..")
            break

        elif int(user_input) == answer:
            nex.say("Correct!")
            nex.runAndWait()
        else:
            nex.say(f"Incorrect. The correct answer is {answer}.")
            nex.runAndWait()

close = lambda:windows.destroy()

def create_window():


    label = ttk.Label(windows, text="Select an option:\nType EXIT in the Answer Box to EXIT")
    label.pack(pady=10)

    quiz_button = ttk.Button(windows, text="Take Quiz", command=multiply_questions)
    quiz_button.pack(pady=5)

    exit_button = ttk.Button(windows, text="Stop Questions", command=close)
    exit_button.pack(pady=3)



def tables():
    nex.say('Need To Learn Multiplication Tables, huh?')
    nex.say('I am Here To Help You')
    nex.say('I will ask you random questions, try to answer them')
    nex.runAndWait()
    create_window()


tables()

windows.mainloop()
