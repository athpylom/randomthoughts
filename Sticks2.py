def stMath(num1, num2):
    return (num1+num2)%5

class node:
    def __init__(self, l1, l2, r1, r2, turn, parent):
        self.l1 = l1
        self.l2 = l2
        self.r1 = r1
        self.r2 = r2
        self.turn = turn
        self.childlist = []
        self.parent = parent

    def getParent(self):
        return self.parent

    def setChild(self, child):
        self.childlist.append(child)

    def getChilds(self):
        return self.childlist

    def get(self):
        return self.l1,self.l2,self.r1,self.r2,self.turn

    def gen(self):
        if (self.turn == 0):
            if (self.l1 == 0 and self.l2 % 2 == 0 and self.l2 != 0):
                self.childlist.append(node(int(self.l2 / 2), int(self.l2 / 2), self.r1, self.r2, 1,self))
            elif (self.l1 != 0):
                self.childlist.append(
                    node(self.l1, self.l2, stMath(self.r1, self.l1), self.r2,
                         1,self))
                self.childlist.append(
                    node(self.l1, self.l2, self.r1, stMath(self.r2, self.l1),
                         1,self))

            if (self.l2 == 0 and self.l1 % 2 == 0 and self.l1 != 0):
                self.childlist.append(
                    node(int(self.l1 / 2), int(self.l1 / 2), self.r1, self.r2, 1,self))
            elif (self.l2 != 0):
                self.childlist.append(
                    node(self.l1, self.l2, stMath(self.r1, self.l2), self.r2,
                         1,self))
                self.childlist.append(
                    node(self.l1, self.l2, self.r1, stMath(self.r2, self.l2),
                         1,self))

            if (self.l1 == 0 and self.l2 == 0):
                self.childlist.append(node(0, 0, 0, 0, 1,self))
        else:
            if (self.r1 == 0 and self.r2 % 2 == 0 and self.r2 != 0):
                self.childlist.append(
                    node(self.l1, self.l2, int(self.r2 / 2), int(self.r2 / 2), 0,self))
            elif (self.l1 != 0):
                self.childlist.append(
                    node(stMath(self.l1, self.r1), self.l2, self.r1, self.r2,
                         0,self))
                self.childlist.append(
                    node(self.l1, stMath(self.l2, self.r1), self.r1, self.r2,
                         0,self))

            if (self.r2 == 0 and self.r1 % 2 == 0 and self.r1 != 0):
                self.childlist.append(
                    node(self.l1, self.l2, int(self.r1 / 2), int(self.r1 / 2), 0,self))
            elif (self.l1 != 0):
                self.childlist.append(
                    node(stMath(self.l1, self.r2), self.l2, self.r1, self.r2,
                         0,self))
                self.childlist.append(
                    node(self.l1, stMath(self.l2, self.r2), self.r1, self.r2,
                         0,self))

            if (self.r1 == 0 and self.r2 == 0):
                self.childlist.append(node(0, 0, 0, 0, 0,self))
        return self.childlist

def iter(Flist, Wlist):
    Wlist2 = []
    for x in Wlist:
        Wlist1 = x.gen()
        for i in Wlist1:
            Wlist2.append(i)
    Wlist1 = []
    for node in Wlist2:
        if CFlist(Flist, node)[0]:
            node.setChild(CFlist(Flist, node)[1])
            Flist.append(node)
        else:
            Flist.append(node)
            Wlist1.append(node)
    return Wlist1


def CFlist(Flist,check):
    for x in range(0,len(Flist)):
        if Flist[x].get() == check.get():
            return True, x
    return False, 0

Flist = []
Wlist = []
Wlist1 = []
n0 = node(0,0,0,0,0, None)
Flist.append(n0)

Flist.append(node(0,0,0,0,1,n0))
Flist.append(node(1,1,1,1,0,n0))

Wlist.append(node(1,1,1,1,0,n0))
lenlist = []
while len(Wlist) != 0:
    lenlist.append(len(Wlist))
    Wlist = iter(Flist,Wlist)
    for p in Wlist:
        print(p.get(),end = " ")
    print("")
for i in Flist:
    print(i.get(),end = " ")
print("")
print(lenlist)