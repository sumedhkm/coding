
"""
a=10
b=10
print(a+b)

a="smith"
b="sumedh"
print(a+b)
"""
class addition:
    def __init__(self,a):
        self.a=a
    def __add__(o1,o2):
        return o1.a+o2.a
        
o1= addition(10)
o2= addition(10)

print("total:",(o1+o2))
