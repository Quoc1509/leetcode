class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        mp = defaultdict(int)
        visit = set()
        for i in range(len(s)):
            if s[i] in mp:
                if i-mp[s[i]] >= 2:
                    for j in range(mp[s[i]]+1, i):
                        temp = s[i] + s[j] + s[i]
                        
                        visit.add(temp)
                    mp[s[i]] = i
            else:
                mp[s[i]]= i
        count = Counter(s)
        for key, item in count.items():
            if item >= 3:
                visit.add(key*3)
        return len(visit)