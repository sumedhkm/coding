"""    
try:
    a = 10 / 0
except Exception as e:
    print(e)
  
try:
     a = 10 / 25
except Exception as e:
     print(e)
else:
    print("a value:",a)

try:
     a = 10 / 25
except Exception as e:
     print(e)
else:
    print("a value:",a)
finally:
    print("thank you")
"""
# Type of Exceptions in Python
print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))

#nameerror exception

try:
   print(10/0)
except ZeroDivisionError as e:
    print("denominator cant be zero")
    
    
    
try:
   a=int("joes")
except ValueError as e:
    print("please enter the value")
    
    
try:
   a=[10,20,30,40]
   print(a[10])
except IndexError as e:
    print("invalid index")
    
try:
    f = open("test.txt2")
except FileNotFoundError:
    print("File Not Found")
else:
    print(f.read())
    
    
    
        
    
    
 
    
    
    
    
    
    