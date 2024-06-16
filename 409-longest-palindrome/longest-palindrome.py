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
                
        for k in map:
            if map[k] % 2 == 0:
                ans += map[k]
            elif map[k] > 1:
                ans += map[k]-1
                flag = 1
            else: 
                flag = 1
        
        if flag == 1:
            ans += 1
            
        return ans
            