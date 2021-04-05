import random
n = random.randint(1, 9)
print (n)
guess = int(input("Enter Your Guess :- "))
chances = 1
while chances < 5:
    print
    
    if guess < n:
        print ("Your Guess was Low : Guess an Number Higher then "+ str( guess))
        chances = chances +1
        guess = int(input("Enter an integer from 1 to 9: "))
    elif guess > n:
        print( "Your Guess was High : Guess an Number Lower then "+ str( guess))
        chances = chances +1
        guess = int(input("Enter an integer from 1 to 9: "))
    else:
        print ("Congratulation Your Answer Was Correct!!")
        chances = chances -1
        break
    print
    
    
    if not chances < 5:
        print("Sorry You Lost all Your Chances")
        
