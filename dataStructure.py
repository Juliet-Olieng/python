# list
# accessing values in alist
list1=["physics","chemistry","197,2000"]
print(list1[0])
list2=[1,2,3,4,5,3,3,6,7,8,9]
print(list2[1:5])
# updating a list
list1[2]=2001
print(list1)
print(list1[2])
# deleting from a list
del list2[3]
print(list2)
# length of a list
print(len(list1))
# concatenate
newList=list1+list2
print(newList)
print(list2*3)
print(3 in list2)
print(max(list2))
print(list2.count(3))
newlist2=list1.insert(2,"lemon")
print(newlist2)

