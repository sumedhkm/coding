#int method
class user:
    def __init__(self,name):
        print("call when new instance created")
        self.name=name
        
    def printall(self):
        print("name:",self.name)
        
        
        
o1=user("sumedh")
o1.printall()
print(o1.__dict__)
o2=user("smith")
o2.printall()
print(o2.__dict__)
print(user.__dict__)


