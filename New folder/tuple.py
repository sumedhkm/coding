a=(1,2.5,True,"ram")
print(a)
print(type(a))
print(a[2])
print(a[-3])
print(a[1:3])
b=list(a)
print(a)
b.append("raja")
print(b)
print(type(b))
a=tuple(b)
print(a)
print(type(a))

for i in a:
    print(i)
if "rama" in a:
    print("ram found")
else:
    print("not found")
print(len(a))

a=(1,)
print(type(a))
del a
a=(1,2,7,4)
b=(5,6,7,8)
c=a+b
print(c)
print(c.count(7))

a=(1 ,2, 7, 4)
b=(5 ,6, 7, 8)
c=(a, b)
print(c)
print(c[0])
print(c[1])
print(c[0][1])
x=('joes',)*10
print(x)
a=(1,2,7,4)
print(min(a))
print(max(a))


























