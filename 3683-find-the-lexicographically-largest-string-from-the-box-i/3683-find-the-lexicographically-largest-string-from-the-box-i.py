class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        res = ''
        extra = len(word) - numFriends +1
        for i in range(len(word)):
            # temp = ''
            # j = i
            # while j < i+extra+1 and j < len(word):
            #     temp += word[j]
            #     j += 1
            res = max(res, word[i:i+extra])
        return res