# for_loop
# find language
# def findLanguage(languages):
#     for language in languages:
#         print(language)
# findLanguage(['french','germany','japaness','swahili'])


# # using range
# for x in range(3,8,2):
#     print(x)


# def numbers(num):
#     for i in num:
#         print(i)
# numbers(range(0,10))


# # Write a function that uses while, if and continue 
# # statements to print all the even numbers between 0 and 50.
# def evenNumber():
#     num=0
#     while num<50:
#         num+=1
#         if num%2==0:
#             print(num,'is even')
#             continue
# evenNumber()
# # primeNumber
# def primeNumber(num):
#     if num<2:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
# num=0
# while(num<=100):
#     if primeNumber(num):
#         print(num)
#     num+=1

# Write a Python function that takes two arguments (a and b) and returns their sum.
# def sum_Num (a,b):
#     if a<=b:
#         sum=a+b
#         return sum
# print(sum_Num(10,12))


# Write a Python function that takes a string as input and returns the string reversed.
# def reverse_String(str):
#     newString=str[::-1]
#     print(newString)
# reverse_String("hello world")


# Write a Python function that takes a list of integers as input and returns the sum of all the integers in the list.
# def list_intergers(list):
#     sum=0 
#     for i in list:
#         sum+=i
#     return sum
# print(list_intergers([11,12,13,14,15]))
# Write a Python function that takes a list of integers as input and returns a new list with all the even numbers removed.
def remove_even(list):
    empty=[]
    for x in list:
        if x %2!=0:
         return empty.append(x)
print(remove_even([1,2,3,4,5,6,7,8,9,10]))

# Write a Python function that takes in a string and returns the number of times each word appears in the string.
def str(str):
    empty=dict()
    words=str.split()
    for word in words:
        if word in empty:
            empty[word]+=1
        else:
            empty[word] =1
    return empty                  
print(str("i love love python python"))

        
# Write a Python function that takes a list of integers as input and returns the highest value in the list.
def  intergers(list):
    largestNum=list[0]
    for num in list:
        if num>largestNum:
            largestNum=num
    print(largestNum)
        
       
intergers([4,5,6,7,8,9,10])

# Write a Python function that takes a list of strings as input and returns a new list with all the strings capitalized.
def names(list):
    nameUpper=[]
    for name in list:
        nameUpper.append(name.capitalize())
    return nameUpper

print(names(['juliet','jane','wendy']))

#sorting a list
def sortedlist(list):
    sorted_names=sorted(list)
    print (sorted_names)
sortedlist(['banana','grapes','apples','capcake'])

#filter names with 'o'
def filternames(list):
    empty=[]
    for name in list:







        

            


