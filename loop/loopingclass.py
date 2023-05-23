# using while loop prime numbers from 1-10
def primeNumber(num):
    if num<2:
        return False
    for i in range(2,num):
        if(num % i==0):
            return False
        return True
    num=0
    while(num<=10):
        if primeNumber(num):
            print(num)
    num+=1
primeNumber(10)

    # grouping ages
def ages ():
    age=[10,12,13,14,17,18,19,20,24]
    for ages in age:
        if ages<17:
            print('an a teenager')
        else:
            print("am an adult")
ages()


    
#   we will calculate the square of a number if it greater than 5 
def squaresOfNum(num):
    for nums in num:
        if nums>=5:

            print(nums*nums)
squaresOfNum([4,5,6,7,8])

#  checking if password corrected is correct
# def passwordCheck(password):
# password=input('enter password')
# if password=="juliet254":
#     print("correct password")
# else:
#     print('wrong password')

def passwordcheck(password):
    if password=="juliet254":
        print("correct password")
    else:
        print('wrong password')
passwordcheck('juliet123')

# user_check using if-elif-else
def checklist(choices):
    for choice in choices:
        if choice==1:
            print('admin')
        elif choice==2:
            print('Editor')
        elif choice==3:
            print('guest')
        else:
            print('wrong entry')
checklist([1,3,4,2,5,1])

# Find a greater number between two numbers
def compareTwoNumbers(num1,num2):
    if num1<=num2:
        if num1==num2:
            print(num1,'and', num2,'are equal')
        else:
            print(num1,'is greater than',num2)
    else:
        print(num1,'is smaller than',num2)
compareTwoNumbers(23,25)

