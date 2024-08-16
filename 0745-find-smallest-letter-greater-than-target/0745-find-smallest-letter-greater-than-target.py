class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)-1
        if target < letters[0] or target >= letters[-1]: return letters[0]
        while l <= r:
            m = (l+r)//2
            if target < letters[m]:
                r = m - 1
            else:
                l = m + 1
        return letters[l]