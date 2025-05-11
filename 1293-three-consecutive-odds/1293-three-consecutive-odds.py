class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i = 0
        while i < len(arr):
            if arr[i] % 2 == 1:
                j = i + 1
                while j < len(arr) and arr[j] % 2 == 1:
                    j += 1
                    if j - i == 3:
                        return True
                i = j
            else: i += 1
        return False