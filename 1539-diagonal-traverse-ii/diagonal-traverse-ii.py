class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        '''
        0,0 
        1,0 0,1
        2,0 1,1 0,2
        3,0 0,3
        4,0 3,1 0,4
        4,1 3,2
        4,2
        4,3
        4,4
        '''
        hashmap = defaultdict(list)
        n = len(nums)
        for i in range(n):
            sub_list = nums[i]
            m = len(sub_list)
            for j in range(m):
                row_col_sum = i + j
                val = nums[i][j]
                hashmap[row_col_sum].append(val)
                
        ans = []
        for key, values in hashmap.items():
            values = values[::-1]
            for value in values:
                ans.append(value)

        return ans