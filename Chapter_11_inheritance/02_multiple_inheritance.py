class employe:
    company = "Visa"
    eCode = 12
class freelancer:
    company = "fiver"
    level = 0
    def upgradeLevel(self):
        self.level+=1
class programmer(employe,freelancer):
    name = "Tanjim"


p = programmer()
p.upgradeLevel()
print(p.level)
print(p.company)