for i in range(2,12):
    print(i)

languages=['java','javaScript','c','c+','PHP']
for i in range(len(languages)):
    print(i, 'is', languages[i])

num=[12,13,14,15,16,17]
count=0
for i in num:
    count+=i
    print('the total value is',count)

# continue
num1=[1,2,3,4,5,6,7,8,9]
for i in num1:
    if i==5:
        continue
    print(i)

for j in num1:
    if j==5:
        break
    print(j)

    #  Print first 10 numbe Print first 10 numbers using a for looprs using a for loop
    def first_ten_numbers():
        for num in range(10):
            print(num)

    
    first_ten_numbers()

    # Print sum of all even numbers from 10 to 20
    def prime_numbers():
        for num in range(10,20):
            if (num %2==0):
                print(num)
    prime_numbers()

    #  Calculate the square of each number of list
    def squares_of_nums(num):
        for nums in num:
            squares=nums **2
            print(squares)

    squares_of_nums(num=[1,2,3,4,5])

#  Calculate the average of list of numbers
    def average_of_numbers(numbers):
        sum=0
        for k in numbers:
            sum=sum+k
            numbers_size=len(numbers)
            average=sum/numbers_size
            print(average)
    
    average_of_numbers(numbers=[10,20,30,40,50])

    



