class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        for s in words:
            temp = 1
            for c in s:
                if c not in allowed:
                    temp = 0
                    break
            count += temp
        return count