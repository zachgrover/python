import random
from Variables131138 import *
def piglatin(names):
    vowels = ['A','E','I','O','U']
    pigLatinList = []
    for each in names:
        if each[0] in vowels:
           pigLatinList  += [each + 'ay']
        else:
            pigLatinList +=  [each[1:] + each[0] + 'ay']
            
    
    return pigLatinList
    
def nameGuesser(names):
    print sorted(names)
    theChosenOne = random.choice(names)
    ri = 0
    while ri != theChosenOne:
        ri = raw_input('Who doth thou thinkest is le chosen one: ')
        if ri > theChosenOne:
            print 'the chosen one is before the name you guessed.'
        elif ri < theChosenOne:
            print ' the chosen one is after le name you guessed.'
        else:
            print 'you guessed le corectamoundo name.'
            