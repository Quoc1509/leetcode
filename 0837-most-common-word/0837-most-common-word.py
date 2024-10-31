class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = []
        cur = ''
        for i in paragraph.lower():
            if i.isalpha():
                cur += i
            else:
                if cur:
                    s.append(cur)
                cur = ''
        if cur:
            s.append(cur)
        ban = set(banned)
        count = Counter(s)
        res = ''
        num = 0
        for key, item in count.items():
            if key not in ban:
                if item > num:
                    num = item
                    res = key
        return res