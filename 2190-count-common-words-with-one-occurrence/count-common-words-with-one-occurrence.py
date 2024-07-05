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
            if k in map2:
                if v == map2[k] == 1:
                    ans += 1
                        
        return ans