from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispal(t):
            return t == t[::-1]
        
        ans = []
        
        def go(start, sumlen, a):
            if sumlen == n:
                ans.append(a[::])
                return
            
            for i in range(start+1, n):
                if ispal(s[start+1:i+1]):
                    a.append(s[start+1:i+1])
                    go(i, sumlen+i-start, a)
                    a.pop()
        
        n = len(s)
        for i in range(n):
            if ispal(s[:i+1]):
                go(i, i+1, [s[:i+1]])
        
        return ans

print(Solution().partition(s = "aab"))
print(Solution().partition(s = "a"))