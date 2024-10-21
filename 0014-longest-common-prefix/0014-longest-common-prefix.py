class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cur = strs[0]
        for i in strs:
            j = 0
            temp = ''
            while j < len(cur) and j < len(i):
                if cur[j] != i[j]:
                    break
                temp += cur[j]
                j += 1
            cur = temp
        return cur