class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False

        n = len(s1)
        m = len(s2)
        if n == 0 or m == 0:
            return False
        if n > m:
            return False

        target_hash = 0
        s1_freqmap = Counter(s1)

        for char in s1:
            hash_value = ord(char)
            target_hash += hash_value

        rolling_hash = 0
        for i in range(n-1):
            rolling_hash += ord(s2[i])
        
        left = 0
        for right in range(n-1, m):
            rolling_hash += ord(s2[right])
            if rolling_hash == target_hash:
                if self.is_permutation(left, right, s1_freqmap, s2):
                    return True
            rolling_hash -= ord(s2[left])
            left += 1

        return False

    def is_permutation(self, left, right, s1_freqmap, s2):
        s2_freqmap = {}
        for i in range(left, right+1):
            if s2[i] not in s2_freqmap:
                s2_freqmap[s2[i]] = 1
            else:
                s2_freqmap[s2[i]] += 1

        return s1_freqmap == s2_freqmap
