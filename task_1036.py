from typing import List

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        

print(Solution().isEscapePossible(blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]))
print(Solution().isEscapePossible(blocked = [], source = [0,0], target = [999999,999999]))