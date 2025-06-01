class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        need to find some way to keep track of the longest substring with unique characters
        possibly use hashmap as a frequency counter: ensure that all frequencies == 1

        probably maintain some kind of sliding window
        sliding window will always keep track of the substring with unique characters

        left and right ptr

        condition: all char frequencies in hashmap == 1

        advance right pointer and add character to frequency map
        check if frequency map meets our condition
        if condition violated, means that char pointed by left pointer violates condition
        advance left pointer until condition is met

        check for current substring length and update max if needed
        tc: o(n) -> one pass using right pointer, left pointer will trail behind right pointer
        sc: o(n) -> hashmap to store frequencies, worst case all characters inside hashmap at one time
        '''

        max_length = 0
        hashmap = defaultdict(int)
        left = 0
        n = len(s)
        for i in range(n):
            char = s[i]
            # add to hashmap
            hashmap[char] += 1
            # make sure condition is met
            if hashmap[char] > 1:
                while hashmap[char] > 1:
                    hashmap[s[left]] -= 1
                    left += 1
            # check substring length
            substring_len = i - left + 1
            max_length = max(max_length, substring_len)

        return max_length