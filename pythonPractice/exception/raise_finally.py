#user deined exception

class SomethingIsWrong(Exception):
    def __init__(self,exceptMess):
        self.exceptMess = exceptMess

    def printException(self):
        print("Exception :"+ self.exceptMess)    



try:
    if "data" == "data":
        raise SomethingIsWrong("Someting went Wrong")
except SomethingIsWrong as e:
    e.printException()

finally:
    print("Hello world")    





