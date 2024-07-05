class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = {}
        map2 = {}
        
        for num in nums1:
            if num in map1:
                map1[num] += 1
            else: 
                map1[num] = 1
        for num in nums2:
            if num in map2:
                map2[num] += 1
            else: 
                map2[num] = 1
                
        ans = []
        
        for k1, v1 in map1.items():
            for k2, v2 in map2.items():
                if k1 == k2:
                    ans += min(v2, v1) * [k1]
        
        
        
        
        
        
        
        
        return ans