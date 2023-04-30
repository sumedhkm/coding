class a:
    def display(self):
        print("i am the display of class a")
        
        
class b(a):
    def display(self):
        print("i am the display of class c")
        
        
class c(a):
    
class d(c,b):
    pass

o=d()
o.display()