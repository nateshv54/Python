#Encapsulation
class product:
    def setPid(self,pid):
        self.pid=pid
    def getPid(self):
        return self.pid
    def setPname(self,pname):
        self.pnmae=pname
    def getPname(self):
        return self.pnmae
    def setCompany(self,company):
        self.company=company
    def getCompany(self):
        return self.company
    def setPrice(self,price):
        self.price=price
    def getPrice(self):
        return self.price
    

p=product()
p.setPid(1001)
p.setPname("S23 Ultra")
p.setPrice(106000)
p.setCompany("Samsung")
print("Product information")
print("{}   {}   {}   {}".format(p.getPid(),p.getPname(),p.getCompany(),p.getPrice()))