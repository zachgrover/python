from __future__ import print_function # must be first in file 
import random

def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess != secret:
        if guess > secret:
            print('Too low - my number was ', secret, '.', sep='')
        else:
             print('Too high - my number was ', secret, '.', sep='')    
    else:
        print('Right on! I was number', guess, end='!\n')

def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'

def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not    
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = False
        print('orange bug in food id()')
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = False
        print('banana bug in food_id()') 
    # Add tests so that all lines of code are visited during test
    
    if works:
        print('food_id passed all tests')
    return works

def f(n):
    if int(n)==n:
       if n%2==0:
          if n%3==0:
            print (str(n) + ' is a multiple of 6 ' )
          else:
              print (str(n) + ' is even ' )
       else:
           print (str(n) + ' is odd '  )
           
    else:
        print (str(n) + ' is not an intiger ' )
def quiz_decimal(,) 
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess != secret:
        if guess > secret:
            print('Too low - my number was ', secret, '.', sep='')
        else:
             print('Too high - my number was ', secret, '.', sep='')    
    else:
        print('Right on! I was number', guess, end='!\n')           