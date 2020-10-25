num1 = input("Enter number 1 " )
num2 = input("Enter number 2 ")
try:
    print("The sum of these numbers is ",
          int(num1) + int(num2))
except Exception as e:
    print(e)

print("This is very important")
