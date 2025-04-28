class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_string = s[0]

        n = len(s)
        for i in range(n):
            odd_palindromes = self.spread(s, i, i)
            even_palindromes = self.spread(s, i, i+1)

            if len(odd_palindromes) > len(max_string):
                max_string = odd_palindromes
            if len(even_palindromes) > len(max_string):
                max_string = even_palindromes

        return max_string
    
    def spread(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1:right]