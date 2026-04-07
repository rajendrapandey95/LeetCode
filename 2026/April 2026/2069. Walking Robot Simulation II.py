class Robot:
    D=["East","North","West","South"]

    def __init__(self,w,h):
        self.m=0; self.i=0
        p=[]; d=[]

        for x in range(w): p+=[(x,0)]; d+=[0]
        for y in range(1,h): p+=[(w-1,y)]; d+=[1]
        for x in range(w-2,-1,-1): p+=[(x,h-1)]; d+=[2]
        for y in range(h-2,0,-1): p+=[(0,y)]; d+=[3]

        d[0]=3
        self.p,self.d=p,d

    def step(self,n):
        self.m=1
        self.i=(self.i+n)%len(self.p)

    def getPos(self):
        return list(self.p[self.i])

    def getDir(self):
        return "East" if not self.m else self.D[self.d[self.i]]
