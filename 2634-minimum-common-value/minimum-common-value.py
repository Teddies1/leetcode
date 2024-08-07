class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        one, two = 0, 0
        
        while one < len(nums1) and two < len(nums2):
            if nums1[one] == nums2[two]:
                return nums1[one]
            elif nums1[one] > nums2[two]:
                two += 1
            else:
                one += 1
                
        return -1