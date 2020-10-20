list1 = [1, 2, "shahrear", "shadhin", "me", 5, 6, 7, 8, 7.89]
for item in list1:
    if str(item).isnumeric() and item > 6:
        print(item)
