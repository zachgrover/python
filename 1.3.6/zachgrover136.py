import random
def roll_two_dice():
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = a + b
    return c
    
def guess_letter():
   a = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j','l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']    
   b = random.choice(a) 
   return b