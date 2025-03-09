class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        l = 0
        res = 0 
        new_colors = colors + colors
        for r in range(1, len(colors)+k-1):
            if new_colors[r] == new_colors[r-1]:
                l = r
            if r-l+1 == k:
                l += 1
                res += 1
        return res
