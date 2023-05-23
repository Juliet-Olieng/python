# convrting to sets
list1=['hello',3.18,23,'john',True,False]
set3=set(list1)
print(set3)

type1=type(set3)
print(type1)

set3.add('juliet')
print(set3)

set3.remove(3.18)
print(set3)

set4={6,7,8}
set4.update({3,4,5})
print(set4)

set1={'sammy','collins','juliet',3.18,True,23}
intersection=set1 &set3
print(intersection)
print(set1.difference(set3))
print(set3.union(set1))


A={1,2,1,3,5,4,6,7,8}
print('the minimum of A is',min(A))
print('the maximum of A is',max(A))


