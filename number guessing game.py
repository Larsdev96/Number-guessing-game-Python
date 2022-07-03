import random

low = int(input("Please enter the low range: "))
high = int(input("Please enter the high range: "))

while low < 0:
    if low < 0:
        print("You cannot use numbers below 0")
        low = int(input("Please enter the low range: "))
    else:
        break



player_choice = int(input("Enter number between {0}-{1}: ".format(low, high)))
while player_choice > high or player_choice < low:
    player_choice = int(input("Enter number between {0}-{1}: ".format(low, high)))
    if player_choice >= low and player_choice <= high:
        break

computer_choice = random.randint(low, high)

while player_choice != computer_choice:
    if computer_choice < player_choice:
        print("Guess lower")
        player_choice = int(input("Enter number between {0}-{1}: ".format(low, high)))
    elif computer_choice > player_choice:
        print("Guess higher")
        player_choice = int(input("Enter number between {0}-{1}: ".format(low, high)))
    elif player_choice == computer_choice:
        break

print("You guessed correctly!")

