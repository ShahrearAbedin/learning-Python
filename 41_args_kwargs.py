# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)
# function_name_print("Shahrear", "Abedin", "Bhuiyan", "Shadhin", "Harry")
def funargs(normal, *args):
    for item in args:
        print(item)
har = ["Shahrear", "Abedin", "Bhuiyan", "Shadhin", "Harry", "The Shadhin"]
normal = 43
funargs(normal, *har)
