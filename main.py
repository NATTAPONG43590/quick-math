#import python libraries for number game
from ast import operator
import json
import random
import os, sys
import glob
import time
from tkinter.messagebox import QUESTION
import numpy as np
import tkinter

#================================ initial variable setup ==================================
score = 0 #initialize score

time_per_question = 30 #initialize time per question
additional_time = 1 #time added per correct answer
terms = np.array(["+","-","x","/"]) #initialize terms
ranges = np.array([[0,50],[0,50],[1,50],[1,50]]) #add sub mul div
#================================= function for game =======================================
class Quiz:
    def __init__(self):
        self.terms_range = random.randint(2,3)
        self.operators = np.array([])
        self.operands = np.array([]) 
        self.operands = np.append(self.operands,int(random.randint(ranges[0][0],ranges[0][1])))
        for i in range(self.terms_range-1):
            self.operators = np.append(self.operators,int(random.randint(3,len(terms)-1)))
            self.operands = np.append(self.operands,int(random.randint(ranges[int(self.operators[i])][0],ranges[int(self.operators[i])][1])))
            while self.operators[i] == 3 and self.operands[i] % self.operands[i-1] != 0 and self.operands[i] % self.operands[i-1] != :
                print("first" , self.operands[i])
            #if value is undivisible by previous value, then change it
                self.operands[i] = int(random.randint(ranges[int(self.operators[i])][0],ranges[int(self.operators[i])][1]))
                print("sec" ,self.operands[i])

#================================= main function ===========================================
q = Quiz()
question = ""
for i in range(len(q.operands-1)):
    if i == 0:
        question += str(int(q.operands[0])) + " "
    else:
        question += terms[int(q.operators[i-1])] + " "
        question += str(int(q.operands[i])) + " "
    
print(question) 
