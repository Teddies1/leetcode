class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        l, r = 0, len(height)
        left_max = 0
        right_max = 1

        left_max = 1
        right_max = 1

        water = left_max - 0 = 1

        left_max = 2
        right_max = 1

        left_max = 2
        right_max = 2

        water = 1 + left_max - 1 = 2

        water = 2 + left_max - 2 = 4
        water = 4 + 1 = 5

        left_max = 3
        right_max = 2

        water = 5 + right_max - 1 = 6
        '''
        left, right = 0, len(height)-1
        left_max = height[left]
        right_max = height[right]
        water = 0
        while left < right:
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += (left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += (right_max - height[right])

        return water