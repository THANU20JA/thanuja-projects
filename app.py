from random import *
computer_guess=randrange(1,100)
while True:
    user=int(input("guess a number:"))
    if user <computer_guess:
        print("its too low:")
    elif  user >computer_guess:
        print("its too high:")
    else:
        print("good genius brainy:")
        break
        
        
