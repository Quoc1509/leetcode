class Solution:
    def maximumLength(self, s: str) -> int:
        count = defaultdict(lambda:defaultdict(int))
        i = 0
        res = -1
        while i < len(s):
            j = i+1
            while j < len(s) and s[i] == s[j]:
                j += 1
            x = j-i
            # print(s[i], x)
            if x > 2:
                res = max(res, x-2)
            if x > 1:
                count[s[i]][x-1] += 2
                if count[s[i]][x-1] >= 3:
                    res = max(res, x-1)
            count[s[i]][x] += 1
            if count[s[i]][x] >= 3:
                res = max(res, x)
            i = j

        # print(count)
        return res     
        

