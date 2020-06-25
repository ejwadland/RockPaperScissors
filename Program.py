import random
from time import sleep

fin = False

while fin != True:
    print("Enter your choice \n 1. Rock \n 2. Paper \n 3. Scissors")

    choice = int(input("Users choice: "))

    while choice > 3 or choice < 1:
        choice = int(input("Error, please enter a valid choice: "))

    if choice == 1:
        name = 'Rock'
    elif choice == 2:
        name = 'Paper'
    else:
        name = 'Scissor'

    print("You have chosen: " + name)

    print("Computer's turn")
    sleep(1)


    cpu_choice = random.randint(1,3)

    while cpu_choice == choice:
        cpu_choice = random.randint(1,3)

    if cpu_choice == 1:
        cpu_name = 'Rock'
    elif cpu_choice == 2:
        cpu_name = 'Paper'
    else:
        cpu_name = 'Scissor'

    print("Computer chose: " + cpu_name)

    sleep(1)

    print(name + " vs " + cpu_name)

    sleep(1)

    if ((choice == 1 and cpu_choice == 2) or (choice == 2 and cpu_choice == 1)):
        print("Paper Wins!")
        result = 'Paper'

    elif ((choice == 1 and cpu_choice == 3) or (choice == 3 and cpu_choice == 1)):
        print("Rock Wins!")
        result = "Rock"

    else:
        print("Scissors Win!")
        result = "Scissors"

    sleep(1)

    if result == name:
        print("YOU WIN!")
    else:
        print("COMPUTER WINS!")

    sleep(1)

    print("Would you like to play again? Y/N")
    answer = input()

    if answer == 'n' or answer == 'N':
        fin = True
    else:
        continue





# End the game

print("Game Over!")