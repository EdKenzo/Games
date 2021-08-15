
import random

range = random.randint(10,50)
number = random.randint(1, range)

print("Enter number in range 1-"+ str(range) + ": " )
chances = 5
while chances > 0 :
    
    if chances == 5:
            print("You have 5 chances.")
    elif chances < 5:
            print("You have " + str(chances) + " guesses left")
    guess = int(input("Guess a number: "))    
    if guess < number:
            print ("Number is higher, try again") 
    elif guess > number:
            print ("Number is lower, try again")
    elif guess == number:
            print("Congrats, you guessed the number!")
            break
    chances -= 1
if chances == 0:
        print("You've run out of chances")
        print("The number was ", number)
        print("Better luck next time")
        
    

