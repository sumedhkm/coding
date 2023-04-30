"""
names={'ram','sam','ravi'}
print(names)
print(type(names))
#access vaues using for loop
for name in names:
    print(name)
#adding new element
names.add('sara')
print(names)

#updat another set of a data
a={'kumar','sundar','suresh'}
names.update(a)
print(names)

names.discard('suresh')
print(names)

names.remove('sara')
print(names)

names.pop()
print(names)

names.clear()
print(names)

names={'ram','sam','ravi','kumar','sundar','suresh'}
print(names)

a={1,2,3,4}
b={"a","b","c","d"}
c=a.union(b)
print(c)
a.update(b)
print(a)
"""
a = {1, 2, 3, 4, 5}
b = {5, 6, 7, 8, 9}
"""
c=a.intersection(b)
print(c)
a.intersection_update(b)
print(a)
"""

a = {5, 6, 7, 8, 9}
b = {5, 6, 7, 8, 9}
c=a.isdisjoint(b)
print(c)

c=a.issubset(b)
print(c)

c=a.issuperset(b)
print(c)


















































