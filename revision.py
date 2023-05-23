# Write a Python program to find the largest element in a list.
def largest_element (list):
    if not list:
       return None
    largest=list[0]
    for number in list:
        if number>largest:
            largest=number
    return largest
print(largest_element([12,45,78,96,10]))

# Write a Python program to reverse a string.
def reverse_string(str):
    return str[::-1]
print(reverse_string("mango"))
# thon program to check whether a given number is prime or not.
def prime_number(numbers):
    if numbers<2:
        return False
    for i in range(2,(numbers**0.5)):
            if numbers%i==0:
                return False
    return True
print(prime_number([10,11,12,13,14,15,16,17,18]))




