class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s)) if len(set(s)) > 0 else ""