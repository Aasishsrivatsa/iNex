import os
import random
from tkinter import *
from tkinter import messagebox, simpledialog
from tkinter.ttk import *
import turtle
import time
import pyttsx3
import playsound
import hashlib
import subprocess


window = Tk()
window.title('iNex')
window.geometry('400x400')

# Start #
############################################################

#Tasks
t1: str = '1. Run a calculator'
t2: str = '2. Tell a joke'
t3: str = '3. Open you Diary'
t4: str = '4. Open ClipBoard'
t5: str = '5. Play Rock Song'
t6: str = '6. Birthday Special'
t7: str = '7. Roll a dice'
t8: str = '8. Tables Upto 20'
t9: str = '9. About'


#Speech
nex = pyttsx3.init()

#Dice
def dice():
    nex.say('Play Time!')
    nex.runAndWait()
    
    result = random.randint(1, 6)
    message = f"The result is {result}"
    
    nex.say(message)
    nex.runAndWait()
    
    messagebox.showinfo("Result", message)
    
#CALC
def Calc():
    try:
        subprocess.run(['python', 'D:\Python projects while bored\CALC.py'], check=True)
    except FileNotFoundError:
        print('CALC.py not found')
    except subprocess.CalledProcessError as e:
        print(f'Error running CALC.py: {e}')


#Joke
def jokes():
    nex.say("Need Some Comedy?  No problem. I'm here")
    nex.runAndWait()
    time.sleep(0.3)
    rn = random.randint(1,2)
    
    def laugh():
        nex.say('HA HA HA HA')
    
    jokeQ1 = 'Why Do You Call The Train A Bubble Gum?'
    jokeA1 = ' Because CHEW CHEW TRAIN !!!'
    
    jokeQ2 = 'What do you call an cow in an earthquake ? '
    jokeA2 = 'You would call it a  Milkshake !!!'
    
    if (rn == 1):
        nex.say(jokeQ1)
        nex.runAndWait()
        time.sleep(0.2)
        nex.say(jokeA1)
        laugh()
        nex.runAndWait()
        
    elif (rn == 2):
        nex.say(jokeQ2)
        nex.runAndWait()
        time.sleep(0.2)
        nex.say(jokeA2)
        laugh()
        nex.runAndWait()
        
#Diary
def diary():
    # Prompt for password
    password = b'QWERTY'  # Use a bytes object for the password
    hashed_password = hashlib.sha256(password).hexdigest()
    verify = simpledialog.askstring(title="Verification", prompt="What's the Password?")

    try:
        # Verify password
        if hashed_password == hashlib.sha256(verify.encode()).hexdigest():
            print('ACCESS GRANTED')

            # Open diary file
            subprocess.run(['notepad.exe', 'Diary.txt'])
        else:
            print('ACCESS DENIED')
            print('Locking Diary')

            # Run the about() function to get the hint
            about()
    except:
        print('Error occurred while verifying password')

        
#ClipBoard
def clipboard():
    nex.say('Opening Clipboard')
    nex.runAndWait()
    file = 'notepad.exe ClipBoard.txt'
    os.system(file)
    nex.say('I will remember anything for you now')
    nex.runAndWait()
       
#MUSIC
def music():
    nex.say('Party Time')
    nex.runAndWait()
    playsound('Music.mp3')
    
#Happy_Birthday

def happy_birthday():
    nex.say('Happy Birthday. Wait am i Too Quick')
    nex.runAndWait()

    name = simpledialog.askstring(title="Question", prompt="What is Your Name")
    d1 = f"Okay {name}, I'm going to sing a birthday song for you."
    nex.say(d1)
    nex.runAndWait()

    age = simpledialog.askinteger(title="Question", prompt="What's Your Current Age?")
    d2 = f"So {name} is {age} years old."
    d3 = f"Let's clap {age} times for {name}!"
    nex.say(d2)
    nex.say(d3)
    nex.runAndWait()
    time.sleep(age)

    nex.say('Okay So Lets Cut The Birthday Cake')
    nex.runAndWait()
    draw_cake(name)

    def draw_cake(name):
        turtle.speed(3)
        turtle.width(5)
        turtle.pencolor('pink')

        # draw cake
        draw_rectangle(100, 50)

        # draw candles
        draw_candles()

        # write name
        turtle.penup()
        turtle.forward(45)
        turtle.write(f'Happy Birthday {name}!', align='center', font=('Arial', 12, 'normal'))
        turtle.backward(45)

        # finish cake
        turtle.right(350)
        nex.say(f"The cake is ready, {name}!")
        nex.say(f"Let's cut it, {name}!")
        nex.runAndWait()

    def draw_rectangle(length, width):
        turtle.pendown()
        for _ in range(2):
            turtle.forward(length)
            turtle.right(90)
            turtle.forward(width)
            turtle.right(90)
        turtle.penup()
        turtle.forward(width / 2)
        turtle.right(90)
        turtle.forward(length)
        turtle.left(90)

    def draw_candles():
        turtle.pencolor('red')
        for _ in range(10):
            turtle.pendown()
            turtle.forward(5)
            turtle.penup()
            turtle.forward(5)
            turtle.left(90)
            turtle.forward(20)
            turtle.right(90)

    
#Tables
def tables():
    nex.say('Need To Learn Tables')
    nex.say('I am Here To Help You')
    nex.runAndWait()
    
    n = 20
    a = 1
    b = 10
    
    for i in range(2, n+1):
        for j in range(a, b+1):
            result = i * j
            nex.say(str(i))
            nex.say('times')
            nex.say(j)
            nex.say('equals')
            nex.say(result)
            nex.runAndWait()


#About

def about():

    message = "I am a Python AI voice assistant. I can do a variety of things, including telling jokes, opening programs, and even singing you a birthday song! \nAnswer this question and I will tell you the hint of your PASSWORD \n ***FIRST YEAR AFTER CHIRST'S BIRTH?***"
    messagebox.showinfo("About", message)
    
    choice = simpledialog.askstring(title="What to do ",prompt="What Should I do")
    
    if (choice == '1'):
        nex.say('Welcome to password recovery')
        nex.say('To Remember your password I will give You A hint')
        nex.runAndWait()
        messagebox.showinfo('Hint','HINT:   KEYOARD LAYOUT ')
    
# End #
############################################################
# UI #

greeting = Label(text="Welcome to iNex")
greeting.pack()



#VERIFY



greeting2 = Label(text = 'I can :\n\n')
greeting2.pack()



#Tasks
task1 = Button(text = t1, command = Calc)

task2 = Button(text = t2, command = jokes)

task3 = Button(text = t3, command = diary)

task4 = Button(text = t4, command = clipboard)

task5 = Button(text = t5, command = music)

task6 = Button(text = t6, command = happy_birthday)

task7 = Button(text = t7, command = dice)

task8 = Button(text = t8, command = tables)

task9 = Button(text = t9, command = about)

task1.pack()
task2.pack()
task3.pack()
task4.pack()
task5.pack()
task6.pack()
task7.pack()
task8.pack()
task9.pack()

#Tasks


nex.say('Greetings. Welcome to iNex')
nex.runAndWait()

window.mainloop()