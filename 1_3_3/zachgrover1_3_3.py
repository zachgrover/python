from __future__ import print_function # use Python 3.0 printing 

def age_limit_output(age):
    '''Step 6a if-else example'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(str(age) + ' is below the age limit.')
    else:
        print(str(age) + ' is old enough.')
    print('Minimum age is ' + str(AGE_LIMIT))
age_limit_output(10)
age_limit_output(16)
def report_grade(percent): 
    '''Step 6b if-else'''
    grade_limit=80 
    if percent < grade_limit:
        print(' A grade of '+ str(percent)+ ' does not show mastery. Seek extra practice or help. ')
    else:
        print('  A grade of ' + str(percent)+  ' shows mastery. Keep up the good work! ') 

def letter_in_word(guess, word):
    
    if guess in word:
        return True
    else:
        return False    
def vowel(letter):
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        return True
    else:
        return False
# should check len(letter)==1
         