import time
# initial = time.time()
# x = 0
# while x < 55:
#     print("Shahrear Abedin Bhuiyan")
#     x += 1
# total_while = time.time() - initial
# print("While loop ran in", total_while)
# init = time.time()
# for i in range(55):
#     print("Shahrear Abedin Bhuiyan")
# total_for = time.time() - init
# print("for loop ran in", total_for)

local_time = time.asctime(time.localtime(time.time()))
print(local_time)

for z in range(10):
    print(f"{z} Shadhin Bhai")
    time.sleep(.5)
