# Snake water gun
import random
lst = ["rock", "paper", "scissor"]
x = 0
you = 0
computer = 0
print("rock=r, paper=p, scissor=s. Ready to challenge computer")
while x <= 9:
    x += 1
    value = input(f"Match:{x}  Insert stone, paper or scissor: ")
    value.lower()
    choice = random.choice(lst)
    print(choice)
    if value == "r" or value == "p" or value == "s":
        if choice == value:
            print("Draw match")
        elif choice == "s" and value == "p":
            you += 1
            print(f"You won, your point: {you}")
        elif choice == "p" and value == "rock":
            computer += 1
            print(f"Computer won, computers point: {computer}")
        elif choice == "p" and value == "s":
            you += 1
            print(f"You won, your point: {you}")
        elif choice == "s" and value == "p":
            computer += 1
            print(f"Computer won, computers point: {computer}")
        elif choice == "s" and value == "rock":
            you += 1
            print(f"You won, your point: {you}")
        elif choice == "rock" and value == "scissor":
            computer += 1
            print(f"Computer won, computers point: {computer}")
    else:
        print("Something error inserted. Please try again")
print(f"\nYour total point: {you}")
print(f"Computers total point: {computer}")
match = you+computer
print(f"Draw match:", 10-match)
if you > computer:
    print("You won the season")
elif you == computer:
    print("The season has been drawn")
else:
    print("Computer won the season")
