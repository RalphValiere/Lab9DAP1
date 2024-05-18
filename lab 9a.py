#NAMES

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

from numpy import random

choices = ['rock', 'paper', 'scissors']

p1 = input('Pick one of rock, paper or scissors: ')

# Choice : rock

p2 = random.choice(choices)

# p2 is scissors. I won!

# Let's play 5 rounds against the computer, in a for loop, to see who is winning
# Best 3!

for round in range(1,6):
    my_choice = input('Pick one of rock, paper or scissors: ')
    computer_choice = random.choice(choices)
    if my_choice == 'rock' and computer_choice == 'paper':
        print('You lost! Computer is better than you! AI will replace you all!')
    elif my_choice == 'rock' and computer_choice == 'scissors':
        print('You might have won this time, but AI will come back for you!')
    elif my_choice == 'paper' and computer_choice == 'rock':
        print('You might have won this time, but AI will come back for you!')
    elif my_choice == 'paper' and computer_choice == 'scissors':
        print('You lost! Computer is better than you! AI will replace you all!')
    elif my_choice == 'scissors' and computer_choice == 'rock':
        print('You lost! Computer is better than you! AI will replace you all!')
    elif my_choice == 'scissors' and computer_choice == 'paper':
        print('You might have won this time, but AI will come back for you!')
    else:
        print('You probably chose an illegal move! That means you lost! Ah Ah Ah!')

# Now, let's add how many player we want to play...

choices = ['rock', 'paper', 'scissors']
number_players = input('Choose the number of players for this game: ')
while number_players.isdigit() == False or int(number_players) > 2:
    print('Please enter an number that is an integer and less than 3. ', 
          'This game can only be played with 2 players or less')
    number_players = input('Choose the number of players for this game: ')    
for round in range(1,6):
    if number_players == '0':
        print('Stop wasting my time! You just dont want to play!')
    elif number_players == '1':
        print(f'Player 1 VS Computer - Round {round}')
        my_choice = input('Pick one of rock, paper or scissors: ')
        computer_choice = random.choice(choices)
        if my_choice == 'rock' and computer_choice == 'paper':
            print('You lost! Computer is better than you! AI will replace you all!')
        elif my_choice == 'rock' and computer_choice == 'scissors':
            print('You might have won this time, but AI will come back for you!')
        elif my_choice == 'paper' and computer_choice == 'rock':
            print('You might have won this time, but AI will come back for you!')
        elif my_choice == 'paper' and computer_choice == 'scissors':
            print('You lost! Computer is better than you! AI will replace you all!')
        elif my_choice == 'scissors' and computer_choice == 'rock':
            print('You lost! Computer is better than you! AI will replace you all!')
        elif my_choice == 'scissors' and computer_choice == 'paper':
            print('You might have won this time, but AI will come back for you!')
        elif my_choice == computer_choice:
            print('A draw? How can a human be equal to an AI?')
        else:
            print('You probably chose an illegal move! That means you lost! Ah Ah Ah!')
    else:
        print(f'Player 1 VS Player 2 - Round {round}')
        playerone = input('Player 1! Pick one of rock, paper or scissors: ')
        playertwo = input('Player 2! Pick one of rock, paper or scissors: ')
        if playerone == 'rock' and playertwo == 'paper':
            print('Player 2 wins!!')
        elif playerone == 'rock' and playertwo == 'scissors':
            print('Player 1 wins!!')
        elif playerone == 'paper' and playertwo == 'rock':
            print('Player 1 wins!!')
        elif playerone == 'paper' and playertwo == 'scissors':
            print('Player 2 wins!!')
        elif playerone == 'scissors' and playertwo == 'rock':
            print('Player 2 wins!!')
        elif playerone == 'scissors' and playertwo == 'paper':
            print('Player 1 wins!!')
        elif playerone == playertwo and playerone in choices:
            print('This is a draw!')
        elif playerone not in choices and playertwo in choices:
            print('Player 1 made an illegal move! Player 2 wins')
        elif playerone in choices and playertwo not in choices:
            print('Player 2 made an illegal move! Player 1 wins')
        elif playerone not in choices and playertwo not in choices:
            print('Both players made an illegal move! This is draw')


# Let's organize this into a function (and increase to 10 rounds)

def rock_paper_sci(number_players):
    while number_players > 2 or number_players < 0:
        print('Please enter an number that is an integer and less than 3. ', 
              'This game can only be played with 2 players or less')
        number_players = input('Choose the number of players for this game: ') 
        number_players = int(number_players)
    for round in range(1,11):
        if number_players == 0:
            print('Stop wasting my time! You just dont want to play!')
        elif number_players == 1:
            print(f'Player 1 VS Computer - Round {round}')
            my_choice = input('Pick one of rock, paper or scissors: ')
            computer_choice = random.choice(choices)
            if my_choice == 'rock' and computer_choice == 'paper':
                print('You lost! Computer is better than you! AI will replace you all!')
            elif my_choice == 'rock' and computer_choice == 'scissors':
                print('You might have won this time, but AI will come back for you!')
            elif my_choice == 'paper' and computer_choice == 'rock':
                print('You might have won this time, but AI will come back for you!')
            elif my_choice == 'paper' and computer_choice == 'scissors':
                print('You lost! Computer is better than you! AI will replace you all!')
            elif my_choice == 'scissors' and computer_choice == 'rock':
                print('You lost! Computer is better than you! AI will replace you all!')
            elif my_choice == 'scissors' and computer_choice == 'paper':
                print('You might have won this time, but AI will come back for you!')
            elif my_choice == computer_choice:
                print('A draw? How can a human be equal to an AI?')
            else:
                print('You probably chose an illegal move! That means you lost! Ah Ah Ah!')
        else:
            print(f'Player 1 VS Player 2 - Round {round}')
            playerone = input('Player 1! Pick one of rock, paper or scissors: ')
            playertwo = input('Player 2! Pick one of rock, paper or scissors: ')
            if playerone == 'rock' and playertwo == 'paper':
                print('Player 2 wins!!')
            elif playerone == 'rock' and playertwo == 'scissors':
                print('Player 1 wins!!')
            elif playerone == 'paper' and playertwo == 'rock':
                print('Player 1 wins!!')
            elif playerone == 'paper' and playertwo == 'scissors':
                print('Player 2 wins!!')
            elif playerone == 'scissors' and playertwo == 'rock':
                print('Player 2 wins!!')
            elif playerone == 'scissors' and playertwo == 'paper':
                print('Player 1 wins!!')
            elif playerone == playertwo and playerone in choices:
                print('This is a draw!')
            elif playerone not in choices and playertwo in choices:
                print('Player 1 made an illegal move! Player 2 wins')
            elif playerone in choices and playertwo not in choices:
                print('Player 2 made an illegal move! Player 1 wins')
            elif playerone not in choices and playertwo not in choices:
                print('Both players made an illegal move! This is draw')


# Let's test with 1 player and then 2 players
rock_paper_sci(1)
rock_paper_sci(2)
rock_paper_sci(0)






