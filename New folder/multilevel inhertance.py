class grandfather:
    def ownhouse(self):
        print("grandpa house")
    
class father(grandfather):
    def ownbike(self):
        print("father's ownbike")
        
class son(father):
    def ownbook(self):
        print("son ownbook")
        
o = son()
o.ownhouse()
o.ownbike()