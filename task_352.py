from typing import List

class Dsu:
    def __init__(self, N: int):
        self.N = N
        self.par = [i for i in range(N)]
        self.size = N * [1]
    
    def get_par(self, x: int) -> int:
        if x == self.par[x]:
            return x
        self.par[x] = self.get_par(self.par[x])
        return self.par[x]
    
    def same(self, x: int, y: int) -> bool:
        return self.get_par(x) == self.get_par(y)
    
    def merge(self, x: int, y: int) -> None:
        x, y = self.get_par(x), self.get_par(y)

        if x == y:
            return
        
        if self.size[x] < self.size[y]:
            x, y = y, x
        
        self.par[y] = x
        self.size[x] += self.size[y]

class SummaryRanges:
    def __init__(self):
        self.mxN = int(1e4+228)
        self.ufo = Dsu(self.mxN)
        self.st = set()
        self.actual = set()
        self.interval = {}

    def addNum(self, value: int) -> None:
        if value in self.st:
            return
        
        self.st.add(value)
        self.interval[value] = [value, value]
        self.actual.add((value, value))
        fl = False

        if value-1 in self.st:
            self.ufo.merge(value, value-1)
            fl = True
        
        if value+1 in self.st:
            self.ufo.merge(value, value+1)

    def getIntervals(self) -> List[List[int]]:
        pass