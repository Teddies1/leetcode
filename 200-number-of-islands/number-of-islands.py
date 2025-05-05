class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ans += 1
                    self.floodfill(grid, i, j)
        
        return ans
    
    def floodfill(self, arr, row, col):
        if row < 0 or col < 0 or row >= len(arr) or col >= len(arr[0]) or arr[row][col] == "0":
            return 
        
        arr[row][col] = "0"

        neighbours = [
            (0, 1),
            (-1, 0),
            (1, 0),
            (0, -1),
        ]

        for dx, dy in neighbours:
            self.floodfill(arr, row + dx, col + dy)
        
        