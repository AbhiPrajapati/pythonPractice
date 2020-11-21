# create an empty list accept 10 no from user and append to the list if it is even


list = []


for i in range(0, 11):
    var = int(input("enter a no"))
    if var % 2 == 0:
        list.append(var)
    else:
        continue

print(list)
