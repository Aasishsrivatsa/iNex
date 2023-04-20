#OOP version of iNex

import os
import random
from tkinter import messagebox, simpledialog, Label, ttk, Tk
import turtle
import time
import pyttsx3
import playsound
import hashlib
import subprocess

class Core:
    tasks = {
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
        self.nex = pyttsx3.init()

    def say(self, text):
        self.nex.say(text)
        self.nex.runAndWait()

    def greet(self):
        greeting = Label(text="Welcome to iNex\nI can :\n\n")
        greeting.pack()

    def make_widgets(self):
        for task_num,task in enumerate(self.tasks, start=1):
            button = ttk.Button(text=self.tasks[task_num], command=self.selector(task_num))
            button.pack()

    def selector(self,tsk_num):
        task_fns = {
            1 : self.open_calculator,
            2 : self.open_diary,
            3 : self.open_clipboard,
            4 : self.play_music,
            5 : self.roll_dice,
            6 : self.multiplication_quiz,
            7 : self.about
        }
        return task_fns[tsk_num]

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
                self.say('ACCESS DENIED')
                self.say('Retry')

        except:
            self.say('Error occurred while verifying password')


    def open_clipboard(self):
        pass

    def play_music(self):
        pass

    def roll_dice(self):
        pass

    def multiplication_quiz(self):
        pass

    def about(self):
        pass

iNex = Core()
iNex.greet()
iNex.make_widgets()
iNex.say("hi, Welcome.")

iNex.window.mainloop()
