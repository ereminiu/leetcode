from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])
        f = [[False for x in range(m)] for y in range(n)]
        used = [[False for x in range(m)] for y in range(n)]
        
        def is_border(x, y): 
            return x == 0 or y == 0 or x == n-1 or y == m-1
        
        def inside(x, y):
            return 0 <= x <= n-1 and 0 <= y <= m-1

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        q = deque()

        for x in range(n):
            for y in range(m):
                if board[x][y] == 'O' and is_border(x, y):
                    q.append((x, y))
        
        while q:
            x, y = q.pop()
            f[x][y], used[x][y] = True, True

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not inside(nx, ny) or used[nx][ny] or board[nx][ny] == 'X':
                    continue

                q.append((nx, ny))

        for x in range(n):
            for y in range(m):
                if not f[x][y]:
                    board[x][y] = 'X'
        
        print(*board, sep='\n')

print(Solution().solve(board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
print(Solution().solve(board = [["X"]]))
print(Solution().solve(board = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]))
print(Solution().solve(board = [["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]))