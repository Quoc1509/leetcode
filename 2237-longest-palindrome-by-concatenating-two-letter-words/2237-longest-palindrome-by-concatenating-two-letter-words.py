class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        res = 0
        extra = 0
        for key, item in count.items():
            if key[0] == key[1]:
                if item % 2 == 0:
                    res += (item*2)
                else:
                    res += (item-1) * 2
                    extra = 2
            else:
                temp = key[1] + key[0]
                if temp in count:
                    res += (min(count[temp], item))*4
                    count[temp] = 0
                    count[key] = 0
        return res+extra