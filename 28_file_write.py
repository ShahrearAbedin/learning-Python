# f = open("shadhin.txt", "a")
# c = f.write("Shadhin is awesome\n")
# print(c)
# f.close()


# Handle read and write together
f = open("shadhin.txt", "r+")
print(f.read())
f.write("Thank you")
