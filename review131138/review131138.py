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