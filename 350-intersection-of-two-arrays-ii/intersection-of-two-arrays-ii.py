class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = {}
        map2 = {}
        
        for num in nums1:
            if num in map1:
                map1[num] += 1
            else: 
                map1[num] = 1
        # for num in nums2:
        #     if num in map2:
        #         map2[num] += 1
        #     else: 
        #         map2[num] = 1
                
        ans = []
        
        
        for k, v in map1.items():
            for num in nums2:
                if num == k and v > 0:
                    ans.append(num)
                    v -= 1
                    
        return ans