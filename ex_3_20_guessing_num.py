import random
print("You will get 5 chances to guess a number between 0 to 10")
num_guess = 5
num = random.randint(0, 10)
while num_guess > 0:
    num_guess = num_guess - 1
    yr_guess = int(input("Guess the hidden number: "))
    if num == yr_guess:
        print("Success you guessed the correct number")
        break
    else:
        if num > yr_guess:
            print("Your number is low and you remaining guess", num_guess)
        else:
            print("Your number is high and you remaining guess", num_guess)
    if num_guess == 0:
        print("The number was", num)
