class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"

        while len(word) < k:
            intermediate_word = self.operation(word)
            word += intermediate_word
        return word[k-1]

    def operation(self, word: str) -> str:
        new_word = ""
        for char in word:
            incremented_ascii = (ord(char) + 1) % 122
            new_word += chr(incremented_ascii)

        return new_word
        