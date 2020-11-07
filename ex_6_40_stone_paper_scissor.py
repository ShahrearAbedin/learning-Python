# Snake water gun
import random
lst = ["stone", "paper", "scissor"]
x = 0
you = 0
computer = 0
print("Stone paper scissor. Ready to challenge computer")
while x <= 9:
    x += 1
    value = input(f"Match:{x}  Insert stone, paper or scissor: ")
    value.lower()
    choice = random.choice(lst)
    print(choice)
    if value == "stone" or value == "paper" or value == "scissor":
        if choice == value:
            print("Draw match")
        elif choice == "stone" and value == "paper":
            you += 1
            print(f"You won, your point: {you}")
        elif choice == "paper" and value == "stone":
            computer += 1
            print(f"Computer won, computers point: {computer}")
        elif choice == "paper" and value == "scissor":
            you += 1
            print(f"You won, your point: {you}")
        elif choice == "scissor" and value == "paper":
            computer += 1
            print(f"Computer won, computers point: {computer}")
        elif choice == "scissor" and value == "stone":
            you += 1
            print(f"You won, your point: {you}")
        elif choice == "stone" and value == "scissor":
            computer += 1
            print(f"Computer won, computers point: {computer}")
    else:
        print("Something error inserted. Please try again")
print(f"Your total point: {you}")
print(f"Computers total point: {computer}")
if you > computer:
    print("You won the season")
elif you == computer:
    print("The season has been drawn")
else:
    print("Computer won the season")