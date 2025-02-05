class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        return count <= 2 and Counter(s1) == Counter(s2)