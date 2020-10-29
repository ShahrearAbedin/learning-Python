inp = int(input("Insert an integer: "))
select = int(input("Insert 0 or 1: "))
rows = 1
if select == 0 or select == 1:
    if select == 0:
        select = False
    else:
        select = True
    if select == True:
        while rows <= inp:
            print(rows*"*")
            rows += 1
    elif select == False:
        while rows <= inp:
            print(inp * "*")
            inp -= 1
else:
    print("Something wrong inserted. Please check again")
