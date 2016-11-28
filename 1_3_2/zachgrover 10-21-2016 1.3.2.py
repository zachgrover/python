def add_tip(total, tip_percent): 
    '''This is a multi-line comment  
       Return the total amount including tip
    '''
    tip = tip_percent*total
    return total + tip
    
def hyp(leg1, leg2):
    legs = leg1 ** 2 + leg2 ** 2 
    hype = legs ** .5 
    return hype
    
def mean(value1, value2, value3):
    totalv = value1 + value2 + value3
    average = totalv / 3.0
    return average
    
def perimeter(b,h):
    p = b * 2 + h * 2 
    return p 