a=[1,2,3,4,5]
print(a)
print(type(a))
a[2]=16
print(a)
print("slicing")
print(a[1:2])
print(a[3])
print(a[2:])
print(a[2:4])
print(a[3:4])
print(a[1:4])
print(a[0:4])

print("---------------")
a=[1,True,"smith",5.6,[1,2,3,4]]
print(a)
print(type(a))
print(a[0],"type is",type(a[0]))
print(a[1],"type is",type(a[1]))
print(a[2],"type is",type(a[2]))
print(a[3],"type is",type(a[3]))
print(a[4],"type is",type(a[4]))
print(a[4][3])
print("---------------")
a=[10,25,35,50]
print(a)
a.clear()
print(a)
a=[10,25,35,50]
b=a.copy()
print(b)
a=[10,25,35,25,50,25]
print(a.count(25))
print(a.index(25))
print(max(a))
print(len(a))
print(min(a))
print(a)
a.pop(2)
print(a)
a=[10,25,35,25,50,25]
a.remove(25)
print(a)
print("---------------")
names=["ram"]
print(names)
names.append("sumo")
names.append("smith")
names.append("kumar")
print(names)
names2=["suriya","sumedh"]
names.extend(names2)
print(names)
names.insert(0,"vijay")
print(names)
print("---------------")
print(list(range(5)))
print(list("sumedn"))
a=[100,25,50,25,85]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=["orange","apple","mango"]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=["orange","apple","mango"]
print(a)
a.sort(key=len)
print(a)
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      