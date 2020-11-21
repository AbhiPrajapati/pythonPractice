#list

mylist = [2**x for x in range(0,10)]
for i in mylist:
    print(i)

#set and frozenset

#set : Unordered collection of unique Elements

myset = {"abhishek","gulshan","ananya","deepak","ram"}
myset.add("sagar")
print(myset)

myset2 = frozenset({"abhishek","gulshan","ananya","deepak","ram"})
# myset2.add("sagar")  thus we cannot update frozenset
print(myset2)

#set 

setis = set([10,10,30,50,70,20])
print(sorted(setis))


#dictionary


list1 = ["name","age","id"]
list2 = ["abhishek","20","Armiet18pa12"]

dictionary = {att:val for att,val in zip(list1,list2)}
print(dictionary)