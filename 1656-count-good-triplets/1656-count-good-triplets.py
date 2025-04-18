class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        nums = [0] * 1001
        for j in range(len(arr)):
            for k in range(j+1, len(arr)):
                if abs(arr[j] - arr[k]) <= b:
                    left1 = arr[j]-a
                    left2 = arr[k]-c
                    right1 = arr[j]+a
                    right2 = arr[k]+c

                    idx_left = max(left1, left2)
                    idx_right = min(1000, right1, right2)
                    if idx_right >= idx_left:
                        res += max(0, nums[idx_right]-(nums[idx_left-1] if idx_left-1 >= 0 else 0))

            for k in range(arr[j], 1001):
                nums[k] += 1
        return res
