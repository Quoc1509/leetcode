class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        board = [1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9]
        res = total = count = 0
        for i in range(len(word)):
            total += board[ord(word[i]) - ord('a')]
            if total % (i+1) == 0: res += 1
            l = 0
            temp = total
            for r in range(i+1, len(word)):
                temp -= board[ord(word[l]) - ord('a')]
                temp += board[ord(word[r]) - ord('a')]
                l+=1
                if temp % (i+1) == 0:
                    res += 1
        return res