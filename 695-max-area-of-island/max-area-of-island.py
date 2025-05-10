class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = self.recurse(grid, i, j, 1)
                    max_area = max(area, max_area)

        return max_area

    def recurse(self, grid, row, col, area):
        n = len(grid)
        m = len(grid[0])

        if row < 0 or row >= n or col < 0 or col >= m:
            return 0
        if grid[row][col] == 0:
            return 0
        
        grid[row][col] = 0

        neighbours = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        for dx, dy in neighbours:
            area += self.recurse(grid, row + dx, col + dy, 1)
        
        return area
    
    '''
    idea is to traverse entire grid
    if we find a land, set current area to 1
    do recursive dfs to get the area of the whole island
    check if area is greater than current max
    '''