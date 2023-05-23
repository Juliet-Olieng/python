# Write a Python program that takes a list of numbers as
# input and outputs the second largest number in the list using
# conditional statements and a for loop.
def second_largest(list):
    empty=[]
    for i in list:
        empty.append(i)
    empty.sort()
    print("second largest element is:",i)
second_largest([])