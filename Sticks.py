def stMath(num1, num2):
    return (num1+num2)%5

class node:
    def __init__(self, l1, l2, r1, r2, turn, parent, index):
        self.l1 = l1
        self.l2 = l2
        self.r1 = r1
        self.r2 = r2
        self.turn = turn
        self.childlist = []
        self.parent = parent
        self.index = index

    def setIndex(self, num):
        self.index = num
    
    def getIndex(self):
        return self.index
    
    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def setChild(self, child):
        self.childlist.append(child)

    def getChilds(self):
        return self.childlist

    def getReduc(self):
        return self.l1,self.l2,self.r1,self.r2,self.turn

    def get(self):
        return self.l1,self.l2,self.r1,self.r2,self.turn,self.parent.getIndex(),self.index

    def gen(self):
        if (self.turn == 0):
            if (self.l1 == 0 and self.l2 % 2 == 0 and self.l2 != 0):
                self.childlist.append(node(int(self.l2 / 2), int(self.l2 / 2), self.r1, self.r2, 1,self,0))
            if (self.l1 != 0 and self.r1 != 0):
                self.childlist.append(
                    node(self.l1, self.l2, stMath(self.r1, self.l1), self.r2,
                         1,self,0))
            if (self.l1 != 0 and self.r2 != 0):
                self.childlist.append(
                    node(self.l1, self.l2, self.r1, stMath(self.r2, self.l1),
                         1,self,0))

            if (self.l2 == 0 and self.l1 % 2 == 0 and self.l1 != 0):
                self.childlist.append(
                    node(int(self.l1 / 2), int(self.l1 / 2), self.r1, self.r2, 1,self,0))
            if (self.l2 != 0 and self.r1 != 0):
                self.childlist.append(
                    node(self.l1, self.l2, stMath(self.r1, self.l2), self.r2,
                         1,self,0))
            if (self.l2 != 0 and self.r2 != 0):
                self.childlist.append(
                    node(self.l1, self.l2, self.r1, stMath(self.r2, self.l2),
                         1,self,0))

            if (self.l1 == 0 and self.l2 == 0):
                self.childlist.append(node(0, 0, 0, 0, 1,self,0))
        else:
            if (self.r1 == 0 and self.r2 % 2 == 0 and self.r2 != 0):
                self.childlist.append(
                    node(self.l1, self.l2, int(self.r2 / 2), int(self.r2 / 2), 0,self,0))
            if (self.r1 != 0 and self.l1 != 0):
                self.childlist.append(
                    node(stMath(self.l1, self.r1), self.l2, self.r1, self.r2,
                         0,self,0))
            if (self.r1 != 0 and self.l2 != 0):
                self.childlist.append(
                    node(self.l1, stMath(self.l2, self.r1), self.r1, self.r2,
                         0,self,0))

            if (self.r2 == 0 and self.r1 % 2 == 0 and self.r1 != 0):
                self.childlist.append(
                    node(self.l1, self.l2, int(self.r1 / 2), int(self.r1 / 2), 0,self,0))
            if (self.r2 != 0 and self.l1 != 0):
                self.childlist.append(
                    node(stMath(self.l1, self.r2), self.l2, self.r1, self.r2,
                         0,self,0))
            if (self.r2 != 0 and self.l2 != 0):
                self.childlist.append(
                    node(self.l1, stMath(self.l2, self.r2), self.r1, self.r2,
                         0,self,0))

            if (self.r1 == 0 and self.r2 == 0):
                self.childlist.append(node(0, 0, 0, 0, 0,self,0))
        return self.childlist

def iter(Flist, Wlist):
    index = len(Flist)
    Wlist2 = []
    for x in Wlist:
        Wlist1 = x.gen()
        for i in Wlist1:
            Wlist2.append(i)
    Wlist1 = []
    for node in Wlist2:
        if CFlist(Flist, node)[0]:
            node.setChild(Flist[CFlist(Flist, node)[1]])
            node.setIndex(index)
            Flist.append(node)
        else:
            node.setIndex(index)
            Flist.append(node)
            Wlist1.append(node)
        index += 1
    return Wlist1


def CFlist(Flist,check):
    for x in range(0,len(Flist)):
        if Flist[x].getReduc() == check.getReduc():
            return True, x
    return False, 0

Flist = []
Wlist = []
Wlist1 = []
lenlist = []
index = 0
n0 = node(0,0,0,0,0, None,0)
n0.setParent(n0)
n0.setChild(n0)
Flist.append(n0)
n1 = node(0,0,0,0,1,n0,1)
n1.setParent(n0)
n1.setChild(n0)
n2 = node(1,1,1,1,0,n0,2)
n2.setParent(n0)
Flist.append(n1)
Flist.append(n2)

Wlist.append(n2)

while len(Wlist) != 0:
    Wlist = iter(Flist,Wlist)
