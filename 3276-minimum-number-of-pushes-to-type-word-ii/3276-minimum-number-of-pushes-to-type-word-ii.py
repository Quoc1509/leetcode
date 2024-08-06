class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        res, tmp = 0, []
        for key, item in count.items():
            tmp.append(item)
        tmp.sort(reverse=True)
        print(tmp)
        c = 0
        for i in tmp:
            res += ((c // 8)+1)*i
            c += 1 
        return res