class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        map1 = {}
        map2 = {}
        ans = 0
        for word in words1:
            if word in map1:
                map1[word] += 1
            else:
                map1[word] = 1
                
        for word in words2:
            if word in map2:
                map2[word] += 1
            else:
                map2[word] = 1
                
        for k, v in map1.items():
            for k2, v2 in map2.items():
                if k == k2 and v == v2 == 1:
                    ans += 1
                        
        return ans