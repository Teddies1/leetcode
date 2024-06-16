# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = (right + left)//2
            ans = isBadVersion(mid)
            if ans:
                right = mid-1
            else:
                left = mid+1                
        return left