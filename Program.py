import random


fin = False

while fin != True:

    # Generate CPU choice
    opp = random.choice(("Rock", "Paper", "Scissors"))

    # Receive user choice
    choice = input("Rock, Paper or Scissors?\n")

    # Rock

    if choice == "Rock" and opp == "Paper":
        print(opp + " - CPU WINS!")
        cont = input("Would you like to play again? Y/N:\n ")
        if cont == "N":
            fin = True
    elif choice == "Rock" and opp == "Scissors":
        print(opp + " - YOU WIN!")
        cont = input("Would you like to play again? Y/N:\n ")
        if cont == "N":
            fin = True
    elif choice == "Rock" and opp == "Rock":
        print(opp + " - IT'S A DRAW!")
        cont = input("Would you like to play again? Y/N:\n ")
        if cont == "N":
            fin = True

    # Paper

    if choice == "Paper" and opp == "Scissors":
        print(opp + " - CPU WINS!")
        cont = input("Would you like to play again? Y/N:\n ")
        if cont == "N":
            fin = True
    elif choice == "Paper" and opp == "Rock":
        print(opp + " - YOU WIN!")
        cont = input("Would you like to play again? Y/N:\n ")
        if cont == "N":
            fin = True
    elif choice == "Paper" and opp == "Paper":
        print(opp + " - IT'S A DRAW!")
        cont = input("Would you like to play again? Y/N:\n ")
        if cont == "N":
            fin = True

    # Scissors

    if choice == "Scissors" and opp == "Rock":
        print(opp + " - CPU WINS!")
        cont = input("Would you like to play again? Y/N:\n ")
        if cont == "N":
            fin = True
    elif choice == "Scissors" and opp == "Paper":
        print(opp + " - YOU WIN!")
        cont = input("Would you like to play again? Y/N:\n ")
        if cont == "N":
            fin = True
    elif choice == "Scissors" and opp == "Scissors":
        print(opp + " - IT'S A DRAW!")
        cont = input("Would you like to play again? Y/N:\n ")
        if cont == "N":
            fin = True

# End the game

print("Game Over!")