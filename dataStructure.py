# list
# accessing values in alist
list1=["physics","chemistry","197,2000"]
print(list1[0])
list2=[1,2,3,4,5,3,3,6,7,8,9]
print(list2[1:5])
list2.sort(reverse=True)
print(list2)
# # updating a list
# list1[2]=2001
print(list1)
print(list1[2])
# # deleting from a list
del list2[3]
print(list2)
# # length of a list
print(len(list1))
# # concatenate
newList=list1+list2
print(newList)
print(list2*3)
print(3 in list2)
print(max(list2))
print(list2.count(3))
newlist2=list1.insert(2,"lemon")
print(newlist2)
# tuple
tuple_1=('hello','python',3.14,1.618,True,False,32,[1,2,3],{1,2,3},{'a':3,'b':5})
# length
print(len(tuple_1))
print(tuple_1[0])
print(type(tuple_1[8]))
# concatenation
tuple_2=tuple_1+('juliet',2022)
print(tuple_2)
rep_tup=(1,2,3,4)
print(rep_tup*2)
print(2 in rep_tup)
print(2 not in rep_tup)
# iteration
rep_tup1=(5,6,7,8,9)
for i in rep_tup1:
    print(i)
# cmp function
def cmp(t1,t2):
    return bool(t1>t2)-bool(t1<t2)
t1=(1,3,5)
t2=(2,4,6)
print(cmp(t1,t2))

def cmp1(t3,t4):
    return bool(t3>t4)-bool(t3<t4)
t3=(5)
t4=(4)
print(cmp1(t3,t4))
