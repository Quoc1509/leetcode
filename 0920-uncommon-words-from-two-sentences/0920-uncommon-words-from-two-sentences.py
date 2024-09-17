class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        count = Counter(s1+s2)
        
        res = []
        for key, item in count.items():
            if item == 1:
                res.append(key)
        return res
