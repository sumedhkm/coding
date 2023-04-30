class father:
    def fishing(self):
        print("fishing in rivers")
    def chess(self):
        print("playing chees from father")
    pass

class mother:
    def cooking(self):
        print("cooking food")
    def chess(self):
        print("playing chees from mother")
    pass

class son(father,mother):
    def ride(self):
        print("riding bicycles")
    pass


o=son()
o.ride()
o.fishing()
o.cooking()
o.chess()