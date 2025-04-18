class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        nums = SortedList()
        for j in range(len(arr)):
            for k in range(j+1, len(arr)):
                if abs(arr[j] - arr[k]) <= b:
                    left1 = arr[j]-a
                    left2 = arr[k]-c
                    right1 = arr[j]+a
                    right2 = arr[k]+c
                    idx_left1 = bisect_left(nums, left1)
                    idx_left2 = bisect_left(nums, left2)
                    idx_right1 = bisect_right(nums, right1)
                    idx_right2 = bisect_right(nums, right2)

                    idx_left = max(idx_left1, idx_left2)
                    idx_right = min(idx_right1, idx_right2)
                    res += max(0, idx_right-idx_left)
                    
            nums.add(arr[j])
        return res
