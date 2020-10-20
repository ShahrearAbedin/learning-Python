while (True):
    user = int(input("Insert an integer number: "))
    if(user > 100):
        print("Success your number is greater then 100")
        break
    else:
        print("Try again")
        continue
