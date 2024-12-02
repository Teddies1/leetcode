class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentencelist = sentence.split()
        n = len(sentencelist)
        m = len(searchWord)
        for i in range(n):
            if searchWord == sentencelist[i][:m]:
                return i+1
            
        return -1