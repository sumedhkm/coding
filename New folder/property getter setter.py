#property decorators getter setter

class student:
    def __init__(self,total):
        self._total=total
    def average(self):
        return self._total/5.0
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self,t):
        if t<0 or t>500:
           print("invalid value can't be change")
        self._total=t
        
o=student(450)
print("total:",o.total)
print("average:",o.average())

o.total=560
print("total:",o.total)
print("average:",o.average())

