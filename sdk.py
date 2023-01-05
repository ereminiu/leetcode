class Solver:
    def __init__(self, grid):
        self.n = 9
        self.grid = grid
        self.rows = [set() for x in range(self.n)]
        self.cols = [set() for x in range(self.n)]
        self.box = [[set() for x in range(3)] for y in range(3)]

        for i in range(self.n):
            for j in range(self.n):
                val = self.grid[i][j]
                
                if not val:
                    continue

                self.rows[i].add(val)
                self.cols[j].add(val)
                self.box[i//3][j//3].add(val)

    def find_empty(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == 0:
                    return (i, j)
        return (-1, -1)

    def isvalid(self, x, y, val):
        return not (val in self.rows[x] or val in self.cols[y] or val in self.box[x//3][y//3])

    #Trying to fill the board
    def solve(self): 
        x, y = self.find_empty()

        if (x, y) == (-1, -1):
            return True
        
        for val in range(1, 10):
            if self.isvalid(x, y, val):
                self.grid[x][y] = val
                self.rows[x].add(val)
                self.cols[y].add(val)
                self.box[x//3][y//3].add(val)
                
                if self.solve():
                    return True
                
                self.grid[x][y] = 0
                self.rows[x].remove(val)
                self.cols[y].remove(val)
                self.box[x//3][y//3].remove(val)
        
        return False
    
    def get_solution(self):
        self.solve()
        return self.grid