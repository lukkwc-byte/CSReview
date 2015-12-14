import math

class Heap():
    def __init__(self, length):
        self.h=[None]*length

    def __str__(self):
        return str(self.h)

    def nextAval(self):
        i=1
        while (self.h[i]!=None):
            i+=1
        return i

    def add(self, data):
        i=Heap.nextAval(self)
        self.h[i]=data
        if i > 1:
            while i > 2 and self.h[math.floor(i/2)] > self.h[i] :
                temp=self.h[i]
                self.h[i]=self.h[math.floor(i/2)]
                self.h[math.floor(i/2)]=temp
                i=math.floor(i/2)


    def removeMin(self):
        i=Heap.nextAval(self)-1
        ret=self.h[1]
        self.h[1]=self.h[i]
        self.h[i]=None
        j=1
        while (self.h[j] > self.h[j*2] or self.h[j] > self.h[j*2+1]):
            switchNode=min(self.h[j*2], self.h[j*2+1])
            newJ=j*2
            if switchNode==self.h[j*2+1]:
                newJ+=1
            self.h[newJ]=self.h[j]
            self.h[j]=switchNode
            j=newJ
            print(j)
            if j == i:
                break
        return ret
        

test=Heap(10)
test.add(20)
test.add(4)
test.add(3)
test.add(5)
test.add(22)
test.add(1)
print(test)
print(test.removeMin())

print(test.removeMin())
print(test.removeMin())


