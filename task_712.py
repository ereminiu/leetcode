class Solution:
    def minimumDeleteSum(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[0 for x in range(m)] for j in range(n)]
        
        dp[0][0] = ord(s[0])+ord(t[0]) if s[0] != t[0] else 0

        pref = ord(t[0])
        for j in range(1, m):
            if s[0] != t[j]:
                dp[0][j] = dp[0][j-1] + ord(t[j])
            else:
                dp[0][j] = pref
            pref += ord(t[j])
        
        pref = ord(s[0])
        for i in range(1, n):
            if s[i] != t[0]:
                dp[i][0] = dp[i-1][0] + ord(s[i])
            else:
                dp[i][0] = pref
            pref += ord(s[i])
        
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = int(1e9+228)

                if s[i] == t[j]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + ord(s[i]) + ord(t[j]))
                
                dp[i][j] = min(dp[i][j], dp[i-1][j] + ord(s[i]), dp[i][j-1] + ord(t[j]))
        
        print(*dp, sep='\n')

        return dp[n-1][m-1]

print(Solution().minimumDeleteSum(s = "sea", t = "eat"))
print(Solution().minimumDeleteSum(s = "delete", t = "leet"))
print(Solution().minimumDeleteSum(s = 'abba', t = 'aboba'))