def add_numbers(a,b):
    sum=a+b
    print("Sum:",sum)
# def numbers(a=7,b=6):
#     sum(a+b)
#     print("Add:",sum)

def info(first_name,last_name):
    print("first_name:",first_name)
    print("last_name:",last_name)
    print("last_name:",last_name,"first_name:",first_name)

def hello(*names):
  for name in names:
      print(f"hello{name}")

def multiply_many(**kwargs):
    answer=1
    for num in kwargs.values():
        answer*=num
        return answer