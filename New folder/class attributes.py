#class attriutes in python

class students():
    name="ramkumar"
    age=25
    
 
#getattr method
print(getattr(students,'name'))
print(getattr(students, 'age'))
print(getattr(students, 'gender','no such attribute found'))

#dot notation
print(students.name)
print(students.age)

setattr(students,'name','sumedh')
print(students.name)

setattr(students,'gender','male')
print(students.gender)

students.city="salem"
print(students.city)

print(students.__dict__)

delattr(students,'city')
print(students.__dict__)


delattr(students,'gender')
print(students.__dict__)

delattr(students,'age')
print(students.__dict__)