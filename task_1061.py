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
        
        if x < y:
            self.par[y] = x
        else:
            self.par[x] = y

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        ufo = Dsu(26)

        def get_ord(c):
            return ord(c)-ord('a')

        n = len(s1)
        for i in range(n):
            ufo.merge(get_ord(s1[i]), get_ord(s2[i]))
        
        ans = ''
        for c in baseStr:
            ans += chr(ufo.get_par(get_ord(c)) + ord('a'))
        
        return ans

print(Solution().smallestEquivalentString(s1 = "parker", s2 = "morris", baseStr = "parser"))
print(Solution().smallestEquivalentString(s1 = "hello", s2 = "world", baseStr = "hold"))
print(Solution().smallestEquivalentString(s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"))