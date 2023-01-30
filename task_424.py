from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def get_ord(c):
            return ord(c) - ord('A')

        n = len(s)
        pref = [[0 for x in range(26)] for y in range(n)]
        pref[0][get_ord(s[0])] = 1
        for i in range(1, n):
            pref[i] = pref[i-1].copy()
            pref[i][get_ord(s[i])] += 1
        
        def get_pref(l, r, c):
            idx = get_ord(c)
            if l == 0:
                return pref[r][idx]
            
            return pref[r][idx]-pref[l-1][idx]
        
        ans = 0

        chars = set(s)
        for i in range(n):
            for c in chars:
                left, right = i-1, n
                while right-left > 1:
                    mid = (left+right) // 2
                    if get_pref(i, mid, c) + k >= mid-i+1:
                        left = mid
                    else:
                        right = mid
                
                ans = max(ans, left-i+1)
        
        return ans

print(Solution().characterReplacement(s = "ABAB", k = 2))
print(Solution().characterReplacement(s = "AABABBA", k = 1))
print(Solution().characterReplacement(s = "ABBB", k = 3))