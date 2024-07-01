class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix, prefix, ans = [1] * len(nums), [1] * len(nums), []
        
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
            
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]
            
        print(prefix, postfix)
        for i in range(len(prefix)):
            ans.append(postfix[i] * prefix[i])
            
        return ans