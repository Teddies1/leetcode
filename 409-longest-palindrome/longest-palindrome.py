class Solution:
    def longestPalindrome(self, s: str) -> int:
        map = {}
        ans = 0
        flag = 0
        for c in s:
            if c not in map:
                map[c] = 1
            else:
                map[c] += 1
                
        for k, v in map.items():
            if v % 2 == 0:
                ans += v
            elif v > 1:
                ans += v-1
                flag = 1
            else: 
                flag = 1
        
        if flag == 1:
            ans += 1
            
        return ans
            