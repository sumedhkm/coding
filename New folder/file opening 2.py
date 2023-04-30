f=open("BBB.txt")
print(f.readline())

f.seek(5)
print(f.readline())

f.close()
