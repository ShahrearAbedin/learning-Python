# a = 6
# b = 5
# c = sum((a, b)) # built in function
def function2(a, b):
    """This is the function which will calculate the average
        and it doesn't work for 3 numbers
    """
    # Above line in a doc string
    average = (a + b) / 2
    return average


x = function2(4, 6)
print(function2.__doc__)
