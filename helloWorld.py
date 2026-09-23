#Guessing game with integers
while True: #Checks int is a int and not str
    userInput = input("Enter a Number ") 
    try:
        userInput = int(userInput)
        break
    except: print("Not a number ")

import random #import random number
x = random.randint(1,10)

if userInput < x:
    print("Too Small ") #infintly prints 'Too Small' ??

elif userInput > x:
    print("Too big ")

else:
    print("Correct ")