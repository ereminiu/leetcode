from typing import List

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = []
        n = len(ages)
        for i in range(n):
            players.append([ages[i], scores[i]])
        
        players.sort()
        # print(players)

        dp = n * [0]
        ans = 0
        for i in range(n):
            dp[i] = players[i][1]
            for j in range(i):
                if players[i][0] >= players[j][0] and players[i][1] >= players[j][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
            
            ans = max(ans, dp[i])
        
        # print(dp)
        
        return ans

print(Solution().bestTeamScore(scores = [1,3,5,10,15], ages = [1,2,3,4,5]))
print(Solution().bestTeamScore(scores = [4,5,6,5], ages = [2,1,2,1]))
print(Solution().bestTeamScore(scores = [1,2,3,5], ages = [8,9,10,1]))