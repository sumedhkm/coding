"""
operators:
1.arthmetic operators
2.assignment operators
3.comparsion operators
4. logical operators
5.idetify operators
6.membership operators
7.bitwise operators
"""
#1.arthmetic operators
print(5+6)
print(5-6)
print(5*6)
print(9/6)
print(5**6)
print(2%6)
print(9//6)

print("enter the first number:")
num1=(input())
print("enter the second number:")
num2=(input())
try:
    print("the sum of two numbers is",int(num1)+int(num2))
except Exception as g:
    print(g)
    print("this is a very important value")


