import random
class Person:
    def __init__(self,name,num):
        self.name = name
        self.num = num

class Player(Person):
    def getInfo(self):
        return (self.name,self.num)

n = list()
for i in range(0,22):
    n.append(random.random())

playerName = ["Hossein", "Maziyar", "Akbar", "Nima", "Mehdi", "Farhad", "Mohammad", "Khashayar",
                "Milad", "Mostafa","Amin", "Saeed", "Pouya", "Pourya", "Reza", "Ali", "Behzad",
                "soheil", "Behrouz", "Shahrouz", "Saman", "Mohsen"]

m = list()
m.extend(n)
m.sort()
mid = m[11]
for i in range(0,22):
    p = Player(playerName[i],n[i])
    I = p.getInfo()
    if I[1] < mid:
        print(I[0],'A')
    else:
        print(I[0],'B')