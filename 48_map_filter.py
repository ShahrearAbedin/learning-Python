num = ["3", "4", "5", "6", "7"]
num = list(map(int, num))
# for i in range(len(num)):
#     num[i] = int(num[i])

# num[2] = num[2]+1
# print(num[2])

# def sq(a):
#     return a*a

# square = list(map(sq, num))
# print(square)

square = list(map(lambda x:x*x, num))
print(square)
