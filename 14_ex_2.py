fst_num = int(input("Insert first number: "))
snd_num = int(input("Insert second number: "))
operator = input("Insert operator: ")
if operator == "+":
    total = fst_num + snd_num
elif operator == "-":
    total = fst_num - snd_num
elif operator == "*":
    total = fst_num * snd_num
elif operator == "/":
    total = fst_num / snd_num
if fst_num == 45 or fst_num == 56:
    total = 98
    print(total)
else:
    print(total)