class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curmax = strs[0]
        for str in strs:
            i = 0
            while i < min(len(str), len(curmax)) and str[i] == curmax[i]:
                i += 1
            if i == 0:
                return ""
            else:
                curmax = curmax[:i]
        
        return curmax