print("You will get 5 chances")
num_guess = 5
while num_guess > 0:
    num = 5
    num_guess = num_guess - 1
    yr_guess = int(input("Guess the hidden number: "))
    if num < num_guess:
        print("Your number is high and you remaining guess", num_guess)
    elif num > num_guess:
        print("Your number is low and you remaining guess", num_guess)
    elif num == yr_guess:
        print("Success you guessed the correct number")
        break
    if num_guess == 0:
        print("The number was", num)

