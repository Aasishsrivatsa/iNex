#OOP version of iNex

import os
import random
from tkinter import messagebox, simpledialog, Label, ttk, Tk
import turtle
import time
import pyttsx3
import playsound
import subprocess
import threading

class Voice:
    def __init__(self):
        self.nex = pyttsx3.init()
        self.lock = threading.Lock()

    def say(self, text):
        def _threaded_say(text):
            with self.lock:
                self.nex.say(text)
                self.nex.runAndWait()

        threading.Thread(target=_threaded_say, args=(text,)).start()


class Core:
    _tasks = {
        1: "Run A Calculator",
        2: "Open your Diary",
        3: "Open A ClipBoard",
        4: "Play Some Music",
        5: "Roll a Dice",
        6: "Multiplication Quiz",
        7: "About"
    }

    def __init__(self):
        self.window = Tk()
        self.window.title("iNex")
        self.window.geometry("400x300")

    def greet(self):
        greeting = Label(text="Welcome to iNex\nI can :\n\n")
        greeting.pack()

    def make_widgets(self):
        for task_num,task in enumerate(self._tasks, start=1):
            button = ttk.Button(text=self._tasks[task_num], command=self.selector(task_num))
            button.pack()

    def selector(self, tsk_num):
        _task_fns = {
            1 : TasksThingy.open_calculator,
            2 : TasksThingy.open_diary,
            3 : TasksThingy.open_clipboard,
            4 : TasksThingy.play_music,
            5 : TasksThingy.roll_dice,
            6 : TasksThingy.multiplication_quiz,
            7 : TasksThingy.about
        }
        return _task_fns[tsk_num]

class Things:
    def open_calculator(self):
        try:
            subprocess.run(['python', 'D:\Python projects while bored\CALC.py'], check=True)
        except FileNotFoundError:
            print('CALC.py not found')
        except subprocess.CalledProcessError as e:
            print(f'Error running CALC.py: {e}')


    def open_diary(self):
        word = 'QWERTY'
        verify = simpledialog.askstring(title="Verification", prompt="What's the Password?")
        try:
            if verify == word:
                print('ACCESS GRANTED')

                subprocess.run(['notepad.exe', 'Diary.txt'])
            else:
                print('ACCESS DENIED \nRetry!')
                Nex.say('ACCESS DENIED')
                Nex.say('Retry')

        except:
            Nex.say('Error occurred while verifying password')


    def open_clipboard(self):
        pass

    def play_music(self):
        pass

    def roll_dice(self):
        pass

    def multiplication_quiz(self):
        quiz = MultiplicationQuiz()
        quiz.run()

    def about(self):
        pass
    
TasksThingy = Things()


class MultiplicationQuiz:
    
    def __init__(self):
        self.Mulwindow = Tk()
        self.Mulwindow.title("Multiplication Quiz")
        self.Mulwindow.geometry("200x200")

        label = ttk.Label(self.Mulwindow, text="Select an option:\nType EXIT in the Answer Box to EXIT")
        label.pack(pady=10)

        quiz_button = ttk.Button(self.Mulwindow, text="Take Quiz", command=self.multiply_questions)
        quiz_button.pack(pady=5)

        exit_button = ttk.Button(self.Mulwindow, text="Quit", command=self.Mulwindow.destroy)
        exit_button.pack(pady=3)

    def multiply_questions(self):
        while True:
            lst = list(range(1, 11))
            lst.extend(range(11, 21))

            num1 = random.choice(lst)
            num2 = random.choice(lst)

            question = f"What is {num1} x {num2}?"
            answer = num1 * num2

            Nex.say(question)

            user_input = simpledialog.askstring("Answer", question)

            if user_input is None or user_input.lower() == "exit":
                Nex.say("exiting..")
                break

            elif int(user_input) == answer:
                Nex.say("Correct!")
            else:
                Nex.say(f"Incorrect. The correct answer is {answer}.")
        time.sleep(0.075)
    def run(self):
        Nex.say('Need To Learn Multiplication Tables, huh?')
        Nex.say('I am Here To Help You')
        Nex.say('I will ask you random questions, try to answer them')
        self.Mulwindow.mainloop()




Nex = Voice()

iNex = Core()
iNex.greet()
iNex.make_widgets()
Nex.say("hi, Welcome.")

iNex.window.mainloop()
