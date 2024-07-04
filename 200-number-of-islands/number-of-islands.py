class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ans += 1
                self.floodfill(grid, i, j, "0")
        
        return ans
    
    def floodfill(self, arr, row, col, char):
        if row < 0 or col < 0 or row >= len(arr) or col >= len(arr[0]) or arr[row][col] == char:
            return 
        
        if arr[row][col] != char:
            arr[row][col] = char
        
        self.floodfill(arr, row+1, col, char)
        self.floodfill(arr, row, col-1, char)
        self.floodfill(arr, row-1, col, char)
        self.floodfill(arr, row, col+1, char)
        