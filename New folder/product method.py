#property method
#property decorators getter setter

class student:
    def __init__(self,total):
        self._total=total
        
    def average(self):
        return self._total/5.0
   
    def getter(self):
        return self._total


    def setter(self,t):
        if t<0 or t>500:
           print("invalid value can't be change")
           self._total=t
        
    total = property(getter ,setter)
       
o=student(450)
print("total:",o.total)
print("average:",o.average())

o.total=578
print("total:",o.total)
print("average:",o.average())

