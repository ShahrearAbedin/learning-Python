# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)
# function_name_print("Shahrear", "Abedin", "Bhuiyan", "Shadhin", "Harry")


# normal arguments will come first
def funargs(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    print("\nNow they are my soldiers")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

her = ["Shahrear", "Abedin", "Bhuiyan", "Shadhin", "Harry", "Sha..din"]
kw = {
    "Shadhin":"Human",
    "Shahrear":"Student",
    "Abedin":"Engineer",
    "Bhuiyan":"Programmer",
    "Sha..din":"CEO"
      }
normal = "Hey this is a normal argument and the students are:"
funargs(normal, *her, **kw)
