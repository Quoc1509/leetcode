class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        l, res = 0, 0
        index = deque()
        for r in range(len(nums)):
            if nums[r] % 2 != 0:
                count += 1
                if len(index) >= k:
                    index.popleft()
                index.append(r)
            while count > k:
                if nums[l] %2 != 0:
                    count -= 1
                l += 1
            if count == k:
                res += (index[0]-l+1)
        return res