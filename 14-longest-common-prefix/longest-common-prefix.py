class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curmax = strs[0]
        for str in strs:
            i = 0
            while i < len(str) and i < len(curmax) and str[i] == curmax[i]:
                i += 1
            if i == 0:
                curmax = ""
            else:
                curmax = curmax[:i]
                print(curmax)
        
        
        return curmax