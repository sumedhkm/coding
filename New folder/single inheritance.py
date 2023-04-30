class nokia:
    company="nokia india"
    website="www.nokia-india.com"
    
    def contact_detail(self):
        print("adress:cheery road,salem")
        
class nokia1100(nokia):
    def __init__(self):
        self.name="nokia 1100"
        self.year=1998
        
    def product_details(self):
         print("name:",self.name)
         print("year:",self.year)
         print("wesite:",self.website)
         print("company:",self.company)
         
mobile=nokia1100()
mobile.product_details()
mobile.contact_detail()