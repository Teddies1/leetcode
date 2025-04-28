class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        idea is to, for each element in the array
        generate a left and right pointer than spreads from the middle
        also account for even number palindromes
            left and right pointer = i and i + 1

        "aaa"

        index 0 single char is palindrome
            cannot spread so its just "a"
        try i, i+1 = "aa" cannot spread
        
        index 1 single char is palindrome
            can spread to "aaa"
        try i, i+1 = "aa" cannot spread

        index 2 single char is palindrome
            cannot spread so its just "a"
         

        '''

        ans = 0
        n = len(s)
        for i in range(n):
            odd_palindromes = self.spread(s, i, i)
            even_palindromes = self.spread(s, i, i+1)

            ans += odd_palindromes + even_palindromes
        return ans
    
    def spread(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

        return count