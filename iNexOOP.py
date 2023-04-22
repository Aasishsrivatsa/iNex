#OOP version of iNex
import os
from tkinter import messagebox, simpledialog, Label, ttk, Tk
from playsound import playsound
import threading

class Voice:
    import pyttsx3
    #Related to Voice
    def __init__(self):
        self.Nex = self.pyttsx3.init()
        self.Nex.setProperty("rate",225)
        self.lock = threading.Lock()

    def say(self, text):
        #Making say() a threaded function; improves responsiveness of I/O tasks, like GUI
        def _threaded_say(text):
            with self.lock:
                self.Nex.say(text)
                self.Nex.runAndWait()

        threading.Thread(target=_threaded_say, args=(text,)).start()

    def say_sync(self, text):
        #Made for synchronisation of the say() function
        #Sync process for reliability at cases
        self.Nex.say(text)
        self.Nex.runAndWait()




class _Core:
    #Heart of the program
    #Dictionary to choose task, instead of if,elif,else
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
        #initialisation of the GUI and startup tasks

        
        Nex.say("hi, Welcome.")

        self.window = Tk()
        self.window.title("iNex")
        self.window.geometry("400x300")

        greeting = Label(text="Welcome to iNex\nI can :\n\n")
        greeting.pack()

        #makes buttons
        for task_num,task in enumerate(self._tasks, start=1):
            button = ttk.Button(text=self._tasks[task_num], command=self._selector(task_num))
            button.pack()

    def _selector(self, tsk_num):
        #selects what the button does
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


class CallTasks:
    import subprocess
    import random
    #Specialised Tasks

    def open_calculator(self):
        #opens Calculator
        Nex.say('Opening Calculator')
        
        if os.path.exists("CALC.py"):
            try:
                self.subprocess.call(["python", "CALC.py"])
            except OSError as e:
                print("Error: ", e)
        else:
            Nex.say("The CALC.py file does not exist in the current directory.")


    def open_diary(self):
        #makes and opens diary, doesnt make if exists
        word = 'QWERTY'
        Nex.say("What's the Password?")
        verify = simpledialog.askstring(title="Verification", prompt="What's the Password?")
        
        try:
            if verify == word:
                Nex.say('ACCESS GRANTED')

                self.subprocess.run(['notepad.exe', 'Diary.txt'])
            else:
                print('ACCESS DENIED \nRetry!')
                Nex.say('ACCESS DENIED')
                Nex.say('Retry')

        except:
            Nex.say('Error occurred while verifying password')


    def open_clipboard(self):
        #name explains
        Nex.say('Opening Clipboard')
        self.subprocess.run(['notepad.exe', 'ClipBoard.txt'])

    def play_music(self):
        #name explains
        playsound('Music.mp3')

    def roll_dice(self):
        #name explains
        Nex.say_sync('Rolling Dice')
        
        result = self.random.randint(1, 6)
        message = f"The result is {result}"
        
        Nex.say(message)
        
        messagebox.showinfo("Result", message)

    def multiplication_quiz(self):
        #soo big that it has its own class, this method just initialises and runs it
        quiz = MultiplicationQuiz()

    def about(self):
        pass

#useful for calling, nothing to be initialised
TasksThingy = CallTasks()


class MultiplicationQuiz:
    import random
    #for game exculsively
    def __init__(self):
        #makes window,GUI and says msg upon initialisation
        self.Mulwindow = Tk()
        self.Mulwindow.title("Multiplication Quiz")
        self.Mulwindow.geometry("200x200")

        Nex.say('Need To Learn Multiplication, huh?')

        label = ttk.Label(self.Mulwindow, text="Select an option:\nType EXIT in the Answer Box to EXIT")
        label.pack(pady=10)

        quiz_button = ttk.Button(self.Mulwindow, text="Take Quiz", command=self.multiply_questions)
        quiz_button.pack(pady=5)

        exit_button = ttk.Button(self.Mulwindow, text="Quit", command=self.Mulwindow.destroy)
        exit_button.pack(pady=3)
        
        self.Mulwindow.mainloop()
    
    def multiply_questions(self):
        #quiz master

        while True:
            #makes sure that the questions have a higher probability of being though
            
            num1 = self.random.choice(range(1,11))
            num2 = self.random.choice(range(1,20))

            question = f"What is {num1} x {num2}?"
            answer = num1 * num2

            Nex.say_sync(question)

            user_input = simpledialog.askstring("Answer", question)

            #taking decision, whether correct, wrong or quit
            if user_input == str(answer):
                Nex.say_sync("Correct!")
            elif user_input is None or user_input == "EXIT" or user_input == "":
                Nex.say_sync("Exiting...")
                self.Mulwindow.destroy()
                break
            else:
                Nex.say_sync(f"Incorrect. The correct answer is {answer}.")


#making sure everything wont start automatically when imported as a module
if __name__ == "__main__":
    Nex = Voice()

    iNex = _Core()

    iNex.window.mainloop()
