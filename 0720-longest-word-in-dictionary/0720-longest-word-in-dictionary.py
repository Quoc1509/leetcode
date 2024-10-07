class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        temp = set(words)
        res = ''
        for word in words:
            s = ''
            for i in word:
                s += i
                if s not in temp:
                    break
            
            if len(s) == len(word):
                # print(s, word)
                if len(word) > len(res):
                    res = word
                elif len(word) == len(res):
                    if word < res:
                        res = word
        return res