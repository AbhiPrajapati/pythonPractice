class result:
    def __init__(self,username,maths,science,english):
        self.username = username
        self.maths = maths
        self.science = science
        self.english = english


        self.val = [str(self.maths),str(self.science),str(self.english)]


    def average(self):
        print("average marks : ",((self.maths+self.science+self.english)/3))


    def __str__(self):
        valueString = ""
        for word in self.val:
            valueString +=word+" "
            return valueString
    

Userlist  = []
while True:
    print("---------------------------------------------------------------------------------------------")
    print("Enter your maths,science,english marks for calculation")

    maths = int(input("maths :"))
    science = int(input("science :"))
    english = int(input("english :"))

    username = input("Enter your name \n")
    objectName = result(username,maths,science,english)
    Userlist.append(objectName)
    


    option = input("Restart or not(Y/N)")
    if option.upper() == "Y":
        continue
    elif option.upper() == "N":
        for i in range(0,len(Userlist)):
            print(Userlist[i].username,Userlist[i].average())
            print("-----------------------------------------------------------------------------------")
        break    
    else:
        print("Enter an appropirate option")

            







