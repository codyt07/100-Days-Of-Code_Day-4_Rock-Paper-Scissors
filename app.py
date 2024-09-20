# Day 4 of 100 days  of coding by Dr. Yu. Rock Pappers Scissors!
import random

guesses = ["rock", "paper", "scissors"]
choice = random.choice(guesses)
print("Welcome to Rock, Paper, Scissors!")

while True:
    choice = random.choice(guesses)
    player = input('''\rEnter 0 for Rock, 1 for Paper, 2 for Scissors
\ror Q to quit!
\rGuess: ''')
    print(''' # ''' * 20)
    if (player == '0'):
        print("** You chose Rock!")
        if choice == 'rock':
            print("Tie! Computer also chose Rock!")
        elif choice == 'paper':
            print("Lost! Computer Chose Paper!")
        elif choice == 'scissors':
            print("Win! Computer chose scissors!")

    elif (player == '1'):
        print("** You chose Paper!")
        if choice == 'rock':
            print("Win! Computer chose Rock!")
        elif choice == 'paper':
            print("Tie! Computer Chose Paper!")
        elif choice == 'scissors':
            print("Lost! Computer chose scissors!")

    elif (player == '2'):
        print("** You chose Scissors!")
        if choice == 'rock':
            print("Lost! Computer chose Rock!")
        elif choice == 'paper':
            print("Win! Computer Chose Paper!")
        elif choice == 'scissors':
            print("Tie! Computer chose scissors!")
    

    elif (player.lower() == 'q'):
        print("** Thanks for playing!")
        break
    else:
        print("Invalid Choice!!")
