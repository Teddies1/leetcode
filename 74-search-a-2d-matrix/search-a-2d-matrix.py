class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        if m == 1 and n == 1:
            if matrix[0][0] == target:
                return True
            else:
                return False
            
        col_start, col_end = 0, m - 1
        search_col = 0
        while (col_start <= col_end):
            mid = col_start + ((col_end - col_start)//2)
            if target >= matrix[mid][0]:
                if target <= matrix[mid][n - 1]:
                    search_col = mid
                    break
                else:
                    col_start = mid + 1
            else:
                col_end = mid - 1
        
        row_start, row_end = 0, n - 1

        while (row_start <= row_end):
            mid = row_start + ((row_end - row_start)//2)
            if target == matrix[search_col][mid]:
                return True
            elif target < matrix[search_col][mid]:
                row_end = mid - 1
            else:
                row_start = mid + 1
        
        return False