# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt # standard short name
import random

plt.ion() # sets “interactive on”: figures redrawn when updated

def picks():
    a = [] # make an empty list

    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list      ]
    #    random.choice(   [brackets here to choose from a list] )
    # a += [random.choice([1, 3, 10])]

    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.show()

def days():
    ''' Explain the function here
    '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')
        days()
def roll_hundred_pair():
    list = []
    for i in range(100):
       list += [random.randint(1,6) + random.randint(1,6)] 
    plt.hist(list)
    plt.show()
    
    return list
def dice(n):
    tot = 0
    for i in range(n):
        t = random.randint(1,6)
        tot = t + tot
    return tot 

def matches(ticket, winners):
    hi = 0
    for each in(ticket):
        if each in(winners):
            hi += 1
    return hi       
    
def hangman_display(guessed, secret):
    j = ''    
    for each in secret:
        if each in guessed:
            j += each
        elif each == ' ':
            j += ' '
        else:
            j += '-'
    return j         