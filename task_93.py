from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isvalid(s):
            val = int(s)
            return s == str(val) and val <= 255
        
        n = len(s)
        
        ans = []
        for x in range(n-3):
            for y in range(x+1, n-2):
                for z in range(y+1, n-1):
                    a, b, c, d = s[:x+1], s[x+1:y+1], s[y+1:z+1], s[z+1:]
                    if isvalid(a) and isvalid(b) and isvalid(c) and isvalid(d):
                        ans.append(a + '.' + b + '.' + c + '.' + d)
                    
                    assert a+b+c+d == s
        
        return ans

print(Solution().restoreIpAddresses(s = "25525511135"))
print(Solution().restoreIpAddresses(s = "0000"))
print(Solution().restoreIpAddresses(s = "101023"))