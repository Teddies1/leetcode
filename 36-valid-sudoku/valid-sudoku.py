class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            b = checkRow(board, i)
            c = checkCol(board, i)
            if not b or not c:
                return False
        # 0, 0 0, 3 0, 6
        # 3, 0 3, 3 3, 6
        # 6, 0 6, 3, 6, 6
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i % 3 == 0 and j % 3 == 0:
                    a = checkBox(board, i , j)
                    if not a:
                        return False
        return True
        
    
    
def checkRow(board, index):
    map = {}
    for i in range(len(board)):
        num = board[index][i]
        if num.isdigit() and num not in map:
            map[num] = 1
        elif num.isdigit():
            map[num] += 1
    for k, v in map.items():
        if v > 1:
            return False
    return True


def checkCol(board, index):
    map = {}
    for i in range(len(board)):
        num = board[i][index]
        if num.isdigit() and num not in map:
            map[num] = 1
        elif num.isdigit():
            map[num] += 1
    for k, v in map.items():
        if v > 1:
            return False
    return True

def checkBox(board, row, col):
    map = {}
    for i in range(3):
        for j in range(3):
            num = board[row + i][col + j]
            if num.isdigit() and num not in map:
                map[num] = 1
            elif num.isdigit():
                map[num] += 1
    for k, v in map.items():
        if v > 1:
            return False
    return True