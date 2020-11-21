# def func1():
#     print("Shahrear")
# func2 = func1
# func2()

# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return int
# a = funcret(0)
# print(a)

# def executor(func):
#     func("This")
# executor(print)

def dec1(func1):
    def nowexec():
        print("Executing")
        func1()
        print("Executed")
    return nowexec
@dec1
def who_is_me():
    print("I am a good boy")
# who_is_me = dec1(who_is_me)
who_is_me()
