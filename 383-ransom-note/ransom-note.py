class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note, mag = {}, {}
        for i in ransomNote:
            if i not in note:
                note[i] = 1
            else:
                note[i] += 1
        for i in magazine:
            if i not in mag:
                mag[i] = 1
            else:
                mag[i] += 1
        
        for k, v in note.items():
            if k not in mag:
                return False
            elif v > mag[k]:
                return False
        
        
        return True