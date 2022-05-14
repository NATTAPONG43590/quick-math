#import python libraries for number game
from ast import While, operator
from multiprocessing import Event
import random
import time
from tkinter.messagebox import QUESTION
import numpy as np
import tkinter
import turtle
import os

#================================ initial variable setup ==================================
score = 0 #initialize score
initial_time = 60
btn_click = 1
time_left = initial_time #initialize time per question
additional_time = 2 #time added per correct answer
terms = np.array(["+","-","x","/"]) #initialize terms
select_operation = np.array([1,1,0,0])
final = 10
ranges = np.array([[1,9],[1,9],[1,5],[2,10]]) #add sub mul div
terms_range = np.array([2,30])
answer = None

#================================= function for game =======================================
class Quiz:
    
    def __init__(self):
        self.terms_range = random.randint(terms_range[0],terms_range[1])
        self.operators = np.array([])
        self.operands = np.array([]) 
        self.operands = np.append(self.operands,int(random.randint(ranges[0][0],ranges[0][1])))
        try:
            for i in range(self.terms_range-1):
            
                self.operators = np.append(self.operators,int(random.choice(np.where(select_operation==1)[0])))
                self.operands = np.append(self.operands,int(random.randint(ranges[int(self.operators[i])][0],ranges[int(self.operators[i])][1])))
        except IndexError:
            self.operands = np.array([])
            self.operators = np.array([])
                
q = Quiz()       
def game_start(event):
    if time_left == initial_time:
        countdown()
    next_question()
def next_question():
    global score
    global q
    global time_left
    if time_left > 0:
        e.focus_set()
        usr_input = e.get()
        try:
            usr_input = int(usr_input)
            if check_answer(q,usr_input):
                score += 1
                time_left += additional_time
                errlebel.config(text="")
                correct_label.config(text="Correct!",fg="green")
            else:
                correct_label.config(text="Wrong! the answer is " + str(int(answer)),fg="red")
            e.delete(0,tkinter.END)
            

        except ValueError:
            if usr_input == "":
                correct_label.config(text="")
                errlebel.config(text="Please enter an answer")
            elif type(usr_input) != int:
                correct_label.config(text="")
                errlebel.config(text="Please enter a number")
            e.delete(0,tkinter.END)
    q = Quiz()
    question = "" 
    if q.operands.size == 0:
        label.config(text="please select at least one operation",font=("Arial",15))
        return
    for i in range(len(q.operands-1)):
        if i == 0:
            question += str(int(q.operands[0])) + " "
        else:
            question += terms[int(q.operators[i-1])] + " "
            question += str(int(q.operands[i])) + " "
    label.config(text=question)
    score_label.config(text="Score: " + str(score))
    if score == final:
        tkinter.Tk.destroy(root)
        firework()

def check_answer(quiz,ans):
    global answer
    answer = quiz.operands[0]
    for i in range(1,len(quiz.operands)):
        if(quiz.operators[i-1] == 0):
            answer += quiz.operands[i]
        elif(quiz.operators[i-1] == 1):
            answer -= quiz.operands[i]
        elif(quiz.operators[i-1] == 2):
            answer *= quiz.operands[i]
        elif(quiz.operators[i-1] == 3):
            answer /= quiz.operands[i]
    if(int(ans) == int(answer)):
        return True
    return False  

def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        time_label.config(text="time left  " + str(time_left) + "  s")
        time_label.after(1000, countdown)
    if time_left == 0:
        tkinter.Tk.destroy(root)
def change_operation(num):
    select_operation[num] = 1
def firework():
    screen = turtle.Screen()    
    rootwindow = screen.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
    rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
    screen.bgcolor("black")
    screen.colormode(255)
    t = turtle.Turtle()
    t.speed(10000)
    for i in range(20):
        
        x = random.randint(-250, 250)
        y = random.randint(-250,250)
        t.penup()
        t.goto(x,y)
        t.pendown()
        rs = int(random.randint(0, 255))
        gs = int(random.randint(0, 255))
        bs = int(random.randint(0, 255))
        t.color(rs,gs,bs)
        size = random.randint(2, 8)
        for i in range(5):
                t.forward(size)
                t.backward(size)
                t.left(72)
        #--------------------------------

    for i in range(30):
      x = random.randint(-250, 250)
      y = random.randint(-250,250)
      t.penup()
      t.goto(x,y)
      t.pendown()
      r = int(random.randint(0, 255))
      g = int(random.randint(0, 255))
      b = int(random.randint(0, 255))
      t.color(r, g, b)
      size = random.randint(30, 200)
      for i in range(36):
        t.forward(size)
        t.backward(size)
        t.left(10)
def change_operation():
    global select_operation
    select_operation = np.array([addv.get(),subv.get(),multiv.get(),dividev.get()]) 
#================================= main function ===========================================
q = Quiz()

# create a GUI window
root = tkinter.Tk()
  
# set the title
root.title("Math Game")
# add the background color
# set the size
root.geometry("500x400")
  
# add an instructions label
instructions = tkinter.Label(root, text = "Type your answer and press enter",font = ('Helvetica', 12))
instructions.pack() 
  
# add a score label
score_label = tkinter.Label(root, text = "Press enter to start",
                                      font = ('Helvetica', 12))
score_label.pack()
  
# add a time left label
time_label = tkinter.Label(root, text = "Time left: " + str(time_left), font = ('Helvetica', 12))
                
time_label.pack()
  
# add a label for displaying the colours
label = tkinter.Label(root, font = ('Helvetica', 25), justify="center")
label.pack()
# create the check box widget 
addv = tkinter.IntVar()
subv = tkinter.IntVar()
multiv = tkinter.IntVar()
dividev = tkinter.IntVar() 
add = tkinter.Checkbutton(root, text = "addition", font = ('Helvetica', 10), variable=addv,command=lambda:change_operation())
add.pack()
sub = tkinter.Checkbutton(root, text = "subtraction", font = ('Helvetica', 10), variable=subv,command=lambda:change_operation())
sub.pack()
multi = tkinter.Checkbutton(root, text = "multiply", font = ('Helvetica', 10), variable=multiv,command=lambda:change_operation())
multi.pack()
divide = tkinter.Checkbutton(root, text = "division", font = ('Helvetica', 10), variable=dividev,command=lambda:change_operation())
divide.pack()
change_operation()
# add a text entry box for
# typing in colours
e = tkinter.Entry(root, font = ('Helvetica', 20), justify="center")

# run the 'startGame' function 
# when the enter key is pressed

root.bind('<Return>',game_start)
e.pack()
correct_label = tkinter.Label(root, text = "", font = ('Helvetica', 12), justify="center")
correct_label.pack()
errlebel = tkinter.Label(root, text = "")
errlebel.pack()
# set focus on the entry box
e.focus_set()


# start the GUI
root.mainloop()