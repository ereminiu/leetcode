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
