import random, sys, time

print('''
 ---------------------------------------
| Welcome To Rock Paper Scissors Game!  |
| Rock: r                               |
| Paper: p                              |
| Scissors: s                           |
| Good Luck!                            |
  --------------------------------------
''')
player_score = 0
computer_score = 0
def Game(player_score, computer_score):
    moves = ['r', 'p', 's']               #available moves
    player_wins = ['pr', 'sp', 'rs']      #combination of when player wins

    while True:                           #while user wants to play, ask again
        player_move = input("Your Move: ")#getting user's move
        if player_move not in moves:
            print("Invalid Move.")
            continue
        computer_move = random.choice(moves) #computer makes random choice
        print("Computer's Move: ", computer_move)
        if player_move == computer_move:
            print("Tie")
        elif player_move+computer_move in player_wins:
            player_score += 1  
            print("You Win!")
        else:
            computer_score += 1
            print("You Lose.")
        while True:          #checking for is user wants to play again
            answer = input("Play again? (y/n): ")  
            if answer not in ('y', 'n'):
                print("Invalid Input")
                continue
            if answer == 'y':
                Game(player_score, computer_score) # also we need to pass the variables if we want to use them in next game()                
                sys.exit()
            else:
                print("Your score:", int(player_score))
                print("Computer's score:", int(computer_score))
                print("Goodbye!")
                time.sleep(3)
                sys.exit()
                

Game(player_score, computer_score)
