import random

def compare(usr, comp):
    if (usr == 'Rock' and comp == 'Scissors' or
    usr == 'Paper' and comp == 'Rock' or
    usr == 'Scissors' and comp == 'Paper'):
        print("You won!!!")
    elif (comp == 'Rock' and usr == 'Scissors' or
    comp == 'Paper' and usr == 'Rock' or
    comp == 'Scissors' and usr == 'Paper'):
        print("You lose!!!")
    else:
        print("Draw!!!")

def comp_choice():
    computer_choice = random.choice(["Rock", "Scissors", "Paper"])
    print("Computer choice is: " + computer_choice)
    compare(user_choice, computer_choice)

v = ["Rock", "Scissors", "Paper"]
while True:
    user_choice = input('Type "Rock", "Scissors" or "Paper": ')
    if user_choice == "Exit":
        print("Гудбай, май френд")
        break
    elif user_choice not in v:
        print("Бан")
        continue
    comp_choice()