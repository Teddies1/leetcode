class TrieNode:
    def __init__(self):
        self.alphabet = {}
        self.marker = False

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if c not in cur.alphabet:
                cur.alphabet[c] = TrieNode()
            cur = cur.alphabet[c]
        cur.marker = True

    def search(self, word: str) -> bool:
        cur = self.trie
        for c in word:
            if c not in cur.alphabet:
                return False
            cur = cur.alphabet[c]
        
        return cur.marker

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for c in prefix:
            if c not in cur.alphabet:
                return False
            cur = cur.alphabet[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)