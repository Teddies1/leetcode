class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        idea is to initialise some variables left, right, up down
        then keep appending numbers to our answer in a while loop
        the while loop goes from:
        left to right
        up to down
        right to left
        down to up
        
        number of elements = n*m = k
        while loop will terminate when counter reaches k
        '''
        n = len(matrix)
        m = len(matrix[0])

        num_elements = n*m
        left, right, up, down = 0, m-1, 0, n-1

        counter = 0
        ans = []

        while counter < num_elements:
            for i in range(left, right+1):
                ans.append(matrix[up][i])
                counter += 1
            up += 1
            if counter == num_elements:
                return ans

            for i in range(up, down+1):
                ans.append(matrix[i][right])
                counter += 1
            if counter == num_elements:
                return ans
            right -= 1

            for i in range(right, left-1, -1):
                ans.append(matrix[down][i])
                counter += 1

            down -= 1
            if counter == num_elements:
                return ans
            for i in range(down, up-1, -1):
                ans.append(matrix[i][left])
                counter += 1

            left += 1
            if counter == num_elements:
                return ans
        return ans