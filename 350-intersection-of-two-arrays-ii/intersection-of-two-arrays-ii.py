class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         map1 = {}
        
#         for num in nums1:
#             if num in map1:
#                 map1[num] += 1
#             else: 
#                 map1[num] = 1

#         ans = []
        
#         for k, v in map1.items():
#             for num in nums2:
#                 if num == k and v > 0:
#                     ans.append(num)
#                     v -= 1
                    
#         return ans

        ans = []
    
        nums1.sort()
        nums2.sort()
        
        one, two = 0, 0
        while one < len(nums1) and two < len(nums2):
            if nums1[one] == nums2[two]:
                ans.append(nums1[one])
                one += 1
                two += 1
            elif nums1[one] > nums2[two]:
                two += 1
            else:
                one += 1
            
        return ans