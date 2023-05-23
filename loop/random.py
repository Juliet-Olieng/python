# Declare a function fullName and it print out your full name.
# def my_fullName(first,second,third):
#     names=dict(zip(map(str.lower,first),zip(first,second,third)))
#     x=input("enter you first name").lower()
#     if x in names:
#         print(f'my name is {''.join(names[x])}')
#     else:
#         print('we dont know your full name')
# my_fullName(('juliet','olieng'),('matias','abdo'),('fredrick','elmasary'))







# Declare a function fullName and now it takes firstName, lastName as a parameter and it returns your full - name.
def fullName (name1,name2,name3):
    print(f"My name is {name1} {name2} {name3}")
fullName('juliet','anyango','olieng')

# Declare a function addNumbers and it takes two two parameters and it returns sum.
def addnumbers(num1,num2):
    sum=num1+num2
    return sum
print(addnumbers(12,13))
# An area of a rectangle is calculated as follows: area = length x width. Write a function which calculates areaOfRectangle.
def findArea(length,width):
    area=length*width
    return area
print(findArea(12,20))
# A perimeter of a rectangle is calculated as follows: perimeter= 2x(length + width).
#  Write a function which calculates perimeterOfRectangle.
def findperimeter(length,width):
    sum=length+width
    perimeter=2*sum
    return perimeter
print(findperimeter(12,13))
# A volume of a rectangular prism is calculated as follows: volume = length x width x height. Write a function which calculates volumeOfRectPrism.
# Area of a circle is calculated as follows: area = π x r x r. Write a function which calculates areaOfCircle