#OOP version of iNex

import os
import random
from tkinter import messagebox, simpledialog, Label, ttk
from tkinter import *
import turtle
import time
import pyttsx3
import playsound
import hashlib
import subprocess


class Core:
    tasks = ["1. Run A Calculator",
            "2. Open your Diary",
            "3. Open A ClipBoard",
            "4. Play Some Music",
            "5. Roll a Dice",
            "6. Multiplication Quiz",
            "7. About"]

    def __init__(self):
        self.window = Tk()
        self.window.title("iNex")
        self.window.geometry("400x300")
        self.nex = pyttsx3.init()

    def say(self, text):
        self.nex.say(text)
        self.nex.runAndWait()


    def make_widget(self):
        greeting = Label(text="Welcome to iNex")
        greeting.pack()

        greeting2 = Label(text='I can :\n\n')
        greeting2.pack()
    




iNex = Core()
iNex.make_widget()

#TASKS

def Calc():
    try:
        subprocess.run(['python', 'D:\Python projects while bored\CALC.py'], check=True)
    except FileNotFoundError:
        print('CALC.py not found')
    except subprocess.CalledProcessError as e:
        print(f'Error running CALC.py: {e}')

iNex.say("hi, Welcome.")

def diary():
    password = b'QWERTY'
    hashed_password = hashlib.sha256(password).hexdigest()
    verify = simpledialog.askstring(title="Verification", prompt="What's the Password?")

    try:
        if hashed_password == hashlib.sha256(verify.encode()).hexdigest():
            print('ACCESS GRANTED')

            subprocess.run(['notepad.exe', 'Diary.txt'])
        else:
            print('ACCESS DENIED')
            print('Locking Diary')

            iNex.about()
    except:
        iNex.say('Error occurred while verifying password')



#Tasks
task1 = ttk.Button(text =iNex.tasks[0] , command = Calc)

#task2 = ttk.Button(text = iNex.tasks[1], command = jokes)

#task3 = ttk.Button(text = iNex.tasks[2], command = diary)

#task4 = ttk.Button(text = iNex.tasks[3], command = clipboard)

#task5 = ttk.Button(text = iNex.tasks[4], command = happy_birthday)

#task6 = ttk.Button(text = iNex.tasks[5], command = dice)

#task7 = ttk.Button(text = iNex.tasks[6], command = tables)

#task8 = ttk.Button(text = iNex.tasks[7], command = about)

task1.pack()
#task2.pack()
#task3.pack()
#task4.pack()
#task5.pack()
#task6.pack()
#task7.pack()
#task8.pack()

iNex.window.mainloop()

