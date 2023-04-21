import os
import random
from tkinter import messagebox, simpledialog, Label, ttk, Tk
import turtle
import time
import pyttsx3
import playsound
import subprocess

#Defines the Window

window = Tk()
window.title('iNex')
window.geometry('400x400')

# Start #
############################################################

#list of tasks assigned to a variable which expicitly contains the data type
t1: str = '1. Run a calculator'
t2: str = '2. Tell a joke'
t3: str = '3. Open you Diary'
t4: str = '4. Open ClipBoard'
t5: str = '5. Play Rock Song'
t6: str = '6. Birthday Special'
t7: str = '7. Roll a dice'
t8: str = '8. Tables Upto 20'
t9: str = '9. About'


#Speech module initialisation
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
        subprocess.run(['python', 'CALC.py'], check=True)
    except FileNotFoundError:
        print('CALC.py not found')
    except subprocess.CalledProcessError as e:
        print(f'Error running CALC.py: {e}')


#Joke
def jokes():
    nex.say("Need Some Comedy?  No problem. I'm here")
    nex.runAndWait()
    time.sleep(0.1)
    rn = random.randint(1,2)


    def joke(jokeQ,jokeA):
        nex.say(jokeQ)
        nex.runAndWait()
        time.sleep(0.1)
        nex.say(jokeA)
        nex.say('HA HA HA HA')
        nex.runAndWait()
    
    jokeQ1 = 'Why Do You Call The Train A Bubble Gum?'
    jokeA1 = ' Because CHEW CHEW TRAIN !!!'
    
    jokeQ2 = 'What do you call an cow in an earthquake ? '
    jokeA2 = 'You would call it a  Milkshake !!!'
    
    if (rn == 1):
        joke(jokeQ1,jokeA1)
    elif (rn == 2):
        joke(jokeQ2,jokeA2)
        
#Diary
def diary():
    # Prompt for password
    password = 'QWERTY'
    verify = simpledialog.askstring(title="Verification", prompt="What's the Password?")

    try:
        # Verify password
        if verify == password:
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
    playsound.playsound('Music.mp3')
    
#Happy_Birthday

def happy_birthday():
    nex.say('Happy Birthday. Wait am i Too Quick')
    nex.runAndWait()

    name = simpledialog.askstring(title="Question", prompt="What is Your Name")
    d1 = f"Okay {name}, I'm going to sing a birthday song for you."
    nex.say(d1)
    nex.runAndWait()

    age = simpledialog.askinteger(title="Question", prompt="What's Your Current Age?")
    if age is not None:
        d2 = f"So {name} is {age} years old."
        d3 = f"Let's clap {age} times for {name}!"
        nex.say(d2)
        nex.say(d3)
        nex.runAndWait()
        time.sleep(age)
    elif age is None:
        nex.say("You didn't enter your age. So it's secrets time")

    nex.say('Okay So Lets Cut The Birthday Cake')
    nex.runAndWait()
    

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

    draw_cake(name)

#Tables
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

        user_answer = input(f"Answer to {question}: ")

        if user_answer.lower() == "exit":
            break

        elif int(user_answer) == answer:
            nex.say("Correct!")
            nex.runAndWait()
        else:
            nex.say(f"Incorrect. The correct answer is {answer}.")
            nex.runAndWait()


def create_window():

    windows = Tk()
    windows.title("Multiplication Quiz")
    windows.geometry("300x200")

    # Create label and buttons

    label = ttk.Label(windows, text="Select an option:")
    label.pack(pady=10)
    
    quiz_button = ttk.Button(windows, text="Take Quiz", command=multiply_questions)
    quiz_button.pack(pady=5)

    exit_button = ttk.Button(windows, text="Stop Questions", command=multiply_questions)
    exit_button.pack(pady=3)

def tables():
    nex.say('Need To Learn Multiplication Tables, huh?')
    nex.say('I am Here To Help You')
    nex.say('I will ask you random questions, try to answer them')
    nex.runAndWait()
    create_window()



#About

def about():

    message = "I am a Python assistant. I can do a variety of things, including telling jokes, opening programs, and even singing you a birthday song! \nAnswer this question and I will tell you the hint of your PASSWORD \n ***10 raised to 0 (or) 10^0?***"
    messagebox.showinfo("About", message)
    
    choice = simpledialog.askstring(title="What to do ",prompt="What Should I do")
    
    if (choice == '1'):
        nex.say('Welcome to password recovery')
        nex.say('To Remember your password I will give You A hint')
        nex.runAndWait()
        messagebox.showinfo('Hint','HINT:   DEFAULT KEYOARD LAYOUT ')
    
# End #
############################################################
# UI #

greeting = Label(text="Welcome to iNex")
greeting.pack()



#VERIFY



greeting2 = Label(text = 'I can :\n\n')
greeting2.pack()



#Tasks
task1 = ttk.Button(text = t1, command = Calc)

task2 = ttk.Button(text = t2, command = jokes)

task3 = ttk.Button(text = t3, command = diary)

task4 = ttk.Button(text = t4, command = clipboard)

task5 = ttk.Button(text = t5, command = music)

task6 = ttk.Button(text = t6, command = happy_birthday)

task7 = ttk.Button(text = t7, command = dice)

task8 = ttk.Button(text = t8, command = tables)

task9 = ttk.Button(text = t9, command = about)

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