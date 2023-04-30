class student:
    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.count+=1
        
    def printdetails(self):
        print("name:",self.name,"age:",self.age)
   
    @classmethod 
    def total(cls):
        return cls.count
     
o=student("sumedh",19)
o.printdetails()
print("total admission:",o.total())
a=student("smith",28)
a.printdetails()




print("total admission:",student.total())
print("total admission:",o.total())