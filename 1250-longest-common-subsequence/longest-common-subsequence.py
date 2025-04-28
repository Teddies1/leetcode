class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = [[-1]*(len(text2)) for _ in range(len(text1))]
        self.recurse(text1, text2, 0, 0, cache)

        return cache[0][0]

    def recurse(self, text1, text2, i, j, cache):
        if i == len(text1) or j == len(text2):
            return 0

        if cache[i][j] != -1:
            return cache[i][j]
        if text1[i] == text2[j]:
            cache[i][j] = 1 + self.recurse(text1, text2, i+1, j+1, cache)
        else:
            cache[i][j] = max(self.recurse(text1, text2, i+1, j, cache), self.recurse(text1, text2, i, j+1, cache))

        return cache[i][j]

    '''
    recursion
    if index of text1 or index of text2 reach the end:
        return 0 as we cannot iterate anymore

    if letter of text1 = letter of text2:
        add 1 to longest current subsequence, and recursively check the next character of both texts
    
    otherwise
        recursively check the next character of text1
        recursively check the next character of text2

        return the max value

    memoization
    - idea is we can declare a cache to store previously calculated values
    - if there is a cache hit, simply return value from cache
    - otherwise, proceed as normal and store value in cache
    
    '''