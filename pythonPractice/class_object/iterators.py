#iterators are nothing but __iter__,__next__ method used by for loop internally 

example = ["mango","banana","apple"]

print(dir(example))   # you will see a __iter__ method here
print("-----------------------------------------------------------------------------------------")
iterator = iter(example)

print(iterator)  # here we get object of iter
print("-----------------------------------------------------------------------------------------")

for i in range(0,3):
    print(next(iterator))