class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2:
            return False

        bal = 0
        for i in range(n):
            if s[i] == '(' or locked[i] == '0':
                bal += 1
            else:
                bal -= 1
            
            if bal < 0:
                return False
        
        bal = 0
        for i in range(n-1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                bal += 1
            else:
                bal -= 1
            
            if bal < 0:
                return False
        
        return True

print(Solution().canBeValid(s = "))()))", locked = "010100"))
print(Solution().canBeValid(s = "()()", locked = "0000"))
print(Solution().canBeValid(s = ")", locked = "0"))