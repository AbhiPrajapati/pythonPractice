class Remote():
    def __init__(self):
        self.channel = ['pogo','starplus','sony']
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        return self.channel[self.index]

r = Remote()

print(r.channel)
itr = iter(r)
try:
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
except Exception as e:
    print("Exception :",e)
print("all channels are rendered")        