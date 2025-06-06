class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        # res = ''
        extra = len(word) - numFriends +1
        # for i in range(len(word)):
        #     res = max(res, word[i:i+extra])
        # return res
        l, r = 0, 1
        k = 0
        while r + k < len(word):
            if word[l+k] == word[r+k]:
                k += 1
            elif word[l+k] < word[r+k]:
                l = max(l+k+1, r)
                r = l+1
                k = 0
            else:
                r += k + 1
                k = 0
        return word[l:l+extra]