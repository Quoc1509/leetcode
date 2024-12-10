class Solution:
    def maximumLength(self, s: str) -> int:
        # count = defaultdict(lambda:defaultdict(int))
        # i = 0
        # res = -1
        # while i < len(s):
        #     j = i+1
        #     while j < len(s) and s[i] == s[j]:
        #         j += 1
        #     x = j-i
            
        #     if x > 2:
        #         # there are 3 substrings if x > 2
        #         res = max(res, x-2)
        #     if x > 1:
        #         # there are 2 substrings if x > 1
        #         count[s[i]][x-1] += 2
        #         if count[s[i]][x-1] >= 3:
        #             res = max(res, x-1)
        #     # there is 1 substring for every case
        #     count[s[i]][x] += 1
        #     if count[s[i]][x] >= 3:
        #         res = max(res, x)
        #     i = j
        # return res     
        

# substring: "aaaaa.....a"
#   + if len(substring) > 2: There are 3 substrings with length = len(substring)-2
#   + if len(substring) > 1: There are 2 substrings with length = len(substring)-1
#   + there is a substring with length = len(substring)
        mp = defaultdict(int)
        res, i = -1, 0
        while i < len(s):
            j = i+1
            while j < len(s) and s[i] == s[j]:
                j += 1
            x = j-i
            if j-i >= 3:
                res = max(res, j-i-2)
            mp[s[i:j]] += 1
            i = j
        for key, item in mp.items():
            if item >= 3:
                res = max(res, len(key))
            elif item >= 2 and len(key) > 2:
                res = max(res, len(key)-1)
            elif key[:len(key)-1] in mp:
                res = max(res, len(key)-1)
        return res
