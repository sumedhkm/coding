"""
#list

grocery=("harpic",56,98)
#print(grocery[0:2])
number=[2,7,9,11,3]
#(number.sort())
#number.reverse()
#number.append

number.insert(1,4)
number.remove(2)
number.pop()
number[1]=5
print(number)
#mutable
#immutable
#numbertp=(1,)
#print(numbertp)

#string

a=1
b=2
a,b=b,a
print(a,b)

mystr="very goods"
print(mystr.find("g"))

#dict

d1={}
#print(type(d1))
d2={"krishan":"burger","rohan":"fish","lusu":"dictionary","lokesh":{"B":"maggie","l":"briyani","D":"chicken"}}

print(d2.values())

#if elif else

print("enter your age:")
age=int(input())
if age>18:
    print("u can drive ")
elif age==18: 
    print("we will think")
else:
    print("u can't drive
          
#while loop

i=1

while i<=7:
    print("hj",end="")
    k=1
    while k<=5:
         print("kl",end="")
         k=k+1
    i=i+1
    print()
list1=["sumedh",18,27,"smith",29,"sdsdjnsdjl",9373]
list2=["sum",25,"sumd"]


for i in list1:
    print(i,"sumo")
for i in list2:
    print(i,"smith")



for i in range (1,111):
    if i%2==0:
        print(i)
   
for i in range(1,11):
    if i==3:
        continue
    
    print(i)
    
 
a=int(input("enter first number:"))
b=int(input("enter second number:"))
if a>b:
    print("thambi a b avida greater aa irku") 
else:
    print("thambi b a  aa irku")
    
"""
def function1(a,b):
    """this is a function which takes average"""
    average=(a+b)/2
    print(average)
    return(average)
print(function1.__doc__)


































































