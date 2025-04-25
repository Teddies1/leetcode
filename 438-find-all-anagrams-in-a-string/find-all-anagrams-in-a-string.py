class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        p_hashmap = Counter(p)
        s_hashmap = Counter(s[:m])

        if p_hashmap == s_hashmap:
            ans = [0]
        else:
            ans = []

        left = 0

        for right in range(m, n):
            s_hashmap[s[left]] -= 1
            if s_hashmap[s[left]] == 0:
                s_hashmap.pop(s[left])
            left += 1
            
            s_hashmap[s[right]] = s_hashmap.get(s[right], 0) + 1
            if p_hashmap == s_hashmap:
                ans.append(right - m + 1)
        
        return ans