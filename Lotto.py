import random

def Lotto():
    column = []
    numberList  = list(range(1, 50))
    
    for loop in range(6):
        number = random.choice(numberList)
        column.append(number)
        numberList.remove(number)
        
    return sorted(column)

print(Lotto())
