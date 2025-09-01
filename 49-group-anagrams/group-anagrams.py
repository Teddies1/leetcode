class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None:
            return [[]]

        ans = []
        hashmap = {}
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str in hashmap:
                hashmap[sorted_str].append(string)
            else:
                hashmap[sorted_str] = [string]

        for anagram, words in hashmap.items():
            ans.append(words)
            
        return ans