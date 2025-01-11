class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False    
        if len(s)==k: return True
        count  = Counter(s)
        one, two = 0, 0
        for key, elem in count.items():
            two += (elem//2)
            if elem % 2 == 1:
                one += 1
        if one > k:
            return False
        return True