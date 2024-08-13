class Solution:
    def trap(self, height: List[int]) -> int:
#         left, right, ans = 0, len(height)-1, 0
#         leftMax, rightMax = height[left], height[right]
        
#         while left < right:
#             if leftMax < rightMax:
#                 left += 1
#                 leftMax = max(leftMax, height[left])
#                 ans += leftMax - height[left] 
#             else:
#                 right -= 1
#                 rightMax = max(rightMax, height[right])
#                 ans += rightMax - height[right]
    
            
            
#         return ans
        ans = 0
        n = len(height)
        leftmax, rightmax = [0]*n, [0]*n
        leftmax[0] = height[0]
        rightmax[-1] = height[-1]
        
        for i in range(0, n-1):
            leftmax[i+1] = max(height[i+1], leftmax[i]) 
        
        for i in range(n-1, 0, -1):
            rightmax[i-1] = max(height[i-1], rightmax[i])
            
        for i in range(n):
            if i == 0 or i == n-1:
                continue
            
            
            ans += min(rightmax[i], leftmax[i]) - height[i]
            
        return ans
            