import random, sys

def guessinggame():
    print("Welcome!")
    number = random.randrange(0, 101) #computer picks a random number
    guess = 0
    tries = 0
    while guess != number:            #keep asking until user founds the number
        while True:                   # if guess is not number, ask again
              try:
                 guess = int(input("Make Your Guess!: "))       
              except ValueError:
                 print("It is not a number!")
                 continue
              else:
                 break 
        tries += 1                    #counting every try
        if guess < number:            #if guess less than number print too low
            print("Too Low")
        elif guess > number:
            print("Too High")         #if guess more than number print too high
        else:
            print("Nice! You found it on the {}th try ".format(tries))
            
            while True:               #asking user for play again
                answer = input("Play again? (y/n): ") 
                if answer not in ('y', 'n'):
                    print("Invalid input.")
                    continue
                if answer == 'y':
                    guessinggame()
                else:
                    print("Goodbye")
                    sys.exit()
guessinggame()
            
        
        
        
        
    
    
