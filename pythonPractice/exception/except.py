try:
    data1 = int(input("Enter the First no"))
    data2 = int(input("Enter the Second no"))
    result = data1/data2
except Exception as e:
    print(f"Exception : {e}")
    result = None
print(f"result is {result}")