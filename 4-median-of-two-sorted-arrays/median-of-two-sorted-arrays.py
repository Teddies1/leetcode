class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        array = []
        
        n = len(nums1)-1
        m = len(nums2)-1
        ans, i, j = 0, 0, 0
        while i <= n and j <= m:
            if nums1[i] < nums2[j]:
                array.append(nums1[i])
                i += 1
            else:
                array.append(nums2[j])
                j += 1
        while i <= n:
            array.append(nums1[i])
            i += 1
        while j <= m:
            array.append(nums2[j])
            j += 1
            
        left, right = 0, len(array)-1
        mid = left + ((right - left) // 2)
        if len(array) % 2 == 0:
            ans = (array[mid] + array[mid + 1]) / 2
        else:
            ans = float(array[mid])
        
        return ans
        