class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split(" ")
        
        word_list = [word for word in word_list if word != ""]
        word_list = word_list[::-1]
        print(word_list)
        
        return " ".join(word_list)