class friend():
    def __init__(self,name,des,bonding):
        self.name = name
        self.des = des
        self.bonding = bonding

    def call(self):
        if self.bonding == "good":
            print("We are good friends")
        elif self.bonding ==  "close":
            print("We are close Friends")
        elif self.bonding == "just":
            print("we are just Friends")
        else:
            print("Use correct Keyword For defining your Bounding")

    def about(self):
        print("name : "+self.name)
        print("des : " +self.des)
        print("bonding : "+ self.bonding)        


Deepak = friend("Deepak","He Loves Photography","close")
#Converting ab object of Deepak into dictionary using __dict__
deepakData = Deepak.__dict__ 
Deepak.about()
Deepak.call()

Sagar = friend("Sagar","He is my college friend","good")
sagarData = Sagar.__dict__
Sagar.about()
Sagar.call()

objectList = [deepakData,sagarData]

import json
jsonObject = json.dumps(objectList)
print(jsonObject)
dictObject = json.loads(jsonObject)
print(dictObject)