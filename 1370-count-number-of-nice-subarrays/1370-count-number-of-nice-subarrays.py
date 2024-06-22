class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l, count = 0, 0
        tmp = defaultdict(int)
        save = deque()
        def add(index):
            if len(save) < k:
                save.append(index)
            else:
                save.popleft()
                save.append(index)
        res = 0
        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                count += 1
                add(r)
            while count > k:
                if nums[l] % 2 == 1:
                    count -= 1
                l += 1
            if count == k:
                res += (save[0] - l + 1) 
        return res

