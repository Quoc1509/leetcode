class Solution:
    def reverseWords(self, s: str) -> str:
        res = deque()
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
            else:
                j = i + 1
                while j < len(s) and s[j] != " ":
                    j += 1
                res.appendleft(s[i:j])
                i = j
        return " ".join(res)