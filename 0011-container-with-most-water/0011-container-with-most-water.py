class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, currmax, ans = 0, 0, 0
        right = len(height)-1
        while(left < right):
            width = right - left
            currmax = (min(height[right], height[left])) * width
            ans = max(currmax, ans)
            if (height[right] > height[left]):
                left += 1
            else:
                right -= 1
        return ans
            
        