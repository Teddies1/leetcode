class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        split_sentence = sentence.split(" ")
        if split_sentence[0][0] != split_sentence[-1][-1]:
            return False
        
        n = len(split_sentence)
        
        for i in range(0, n-1):
            if split_sentence[i][-1] != split_sentence[i+1][0]:
                return False
            
        return True