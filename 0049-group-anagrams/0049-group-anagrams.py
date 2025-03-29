class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for s in strs:
            alpha = [0] * 26
            for c in s:
                alpha[ord(c) - ord('a')] += 1
            mp[tuple(alpha)].append(s)
        return list(mp.values())