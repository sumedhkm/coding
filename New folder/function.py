def welcome():
    print("welcome to tutor joes")
    
welcome()
# no return type without arugment function in python
"""
def add():
    a=int(input("enter the value of A:"))
    b=int(input("enter the value of B:"))
    c=a+b
    print("total",c)
    
add()
"""
# no return type without arugment function in python
"""


def sub(a,b):
    c=a-b
    print("difference:",c)
    
sub(25,2)
"""
#return type without arugment function in python
"""
def mul():
    
 a=int(input("enter the value of A:"))
 b=int(input("enter the value of B:"))
 c=a*b
 return c

x=mul()  
print("mul",x)
"""
#return type with arugment function in python

"""
def div(a,b):
    c=a/b
    return c

x=div(25,2)
print("division",x)
"""
#arbitary arguments function in python

"""
def class_10(*students):
    print(students)
    for user in students:
        print(user)
    
class_10("ram","sam","smith","suresh")
"""
# Keyword Arguments Function in Python
"""
def message(name,age):
    print(name,"age is",age)
    
message(age=24,name="raja")
""" 
# Arbitrary Keyword Arguments in Python(**)
"""
def biodata(** data):
    print(data)
    
biodata(name="ramkumar",age=23,gender="male")
"""
 
# Default Parameter Function in Python
"""
def user(name,city="salem"):
    print(name,"is from",city)

user("ram","namakkal")
user("sam")
"""
# Passing a List as an Argument in Function Python
 
def total(marks):
    return sum(marks)

print("total:",total([55,75,80,90,47]))



# recursive function
#1*2*3*4*5=120

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))
 
 
print("Factorial : ", factorial(5))


"""
factorial(5)
5*factorial(4)
5*4*factorial(3)
5*4*3*factorial(2)
5*4*3*2*factorial(1)
5*4*3*2*1
120
print(type(5.0))
print(5.0)
"""


c=lambda a:a+50
print(c(5))

c=lambda a:a/50
print(c(500))













