class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, ans = 0, 0
        dict = {}
        
        for right in range(len(s)):
            if s[right] not in dict:
                dict[s[right]] = 1
            else:
                dict[s[right]] += 1
                while dict[s[right]] > 1:
                    dict[s[left]] -= 1
                    left += 1
            ans = max(ans, right - left + 1)
        
        return ans