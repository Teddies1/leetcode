class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        if not s:
            return 0

        if len(s) == 0:
            return 0
        left = 0
        max_length = 0
        for right in range(len(s)):
            if s[right] not in hashmap:
                hashmap[s[right]] = 1
            else:
                hashmap[s[right]] += 1
            
            window_length = right - left + 1
            max_freq = max(hashmap.values())
            while window_length - max_freq > k:
                hashmap[s[left]] -= 1
                left += 1
                max_freq = max(hashmap.values())
                window_length = right - left + 1
                
            print(hashmap)
            max_length = max(max_length, right - left + 1)

        return max_length
        