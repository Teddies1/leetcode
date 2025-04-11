class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        visited = set()
        for i in range(n):
            for j in range(m):
                ans = self.recurse(board, i, j, 0, word, visited)
                if ans == True:
                    return True
        
        return False
    
    def recurse(self, board, row, col, index, word, visited):
        n = len(board)
        m = len(board[0])
        if index == len(word):
            return True

        if row < 0 or row >= n:
            return False
        if col < 0 or col >= m:
            return False
        if word[index] != board[row][col]:
            return False
        if (row, col) in visited:
            return False
        
        visited.add((row, col))
        neighbours = [
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0),
        ]

        for dx, dy in neighbours:
            if self.recurse(board, row + dx, col + dy, index+1, word, visited) == True:
                return True

        visited.remove((row, col))
        return False