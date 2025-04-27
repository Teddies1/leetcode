class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        the idea is to collect all the rotting oranges

        at each timestamp:
            for each rotting orange:
                rot all 4-adjacent oranges
                collect freshly rotted oranges

        store oranges in queue
        use BFS to rot all adjacent oranges

        return timestamp

        timecomp: O(m*n) becuase worst case traverse all oranges on the grid
        space comp: O(m*n) because worst case might have to store all oranges on the queue 
        
        '''

        queue = []
        timestamp = 0
        n = len(grid)
        m = len(grid[0])
        # first collect all rotten oranges
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))

        # create 4 adjacent list
        neighbours = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        # run bfs on rotten oranges in queue
        while queue:
            # pop each rotten orange from queue
            for i in range(len(queue)):
                x, y = queue.pop(0)
                # check 4 adjacent neighbours if it is orange
                for dx, dy in neighbours:
                    if (0 <= x + dx < n) and (0 <= y + dy < m) and grid[x + dx][y + dy] == 1:
                        # if yes, infect and add to queue
                        grid[x + dx][y + dy] = 2
                        queue.append((x + dx, y + dy))

            # increase timestamp
            if queue:
                timestamp += 1
        
        # check if there are any fresh oranges
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return timestamp