class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        if rows == 0:
            return 0

        num_islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    num_islands += 1
                    self.dfs(grid, i, j)
            
        return num_islands
    
    def dfs(self, grid, row, col):
        neighbours = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]
        rows = len(grid)
        cols = len(grid[0])
        
        if 0 <= row < rows and 0 <= col < cols and grid[row][col] == "1":
            grid[row][col] = "0"
            for dx, dy in neighbours:
                self.dfs(grid, row + dx, col + dy)