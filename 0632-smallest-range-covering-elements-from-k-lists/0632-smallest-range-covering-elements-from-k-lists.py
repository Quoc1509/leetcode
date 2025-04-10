class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        heap = []
        for i in range(len(nums)):
            heappush(heap, (nums[i][0], 1, i))
        arr = []
        while heap:
            num, idx, i = heappop(heap)
            arr.append((num, i))
            if idx < len(nums[i]):
                heappush(heap, (nums[i][idx], idx+1, i))
        # print(arr)

        mp = defaultdict(int)
        l = 0
        res = []
        for r in range(len(arr)):
            mp[arr[r][1]] += 1
            while len(mp) >= len(nums):
                if not res or arr[r][0] - arr[l][0] < res[1] - res[0]:
                    res = [arr[l][0], arr[r][0]]
                mp[arr[l][1]] -= 1
                if mp[arr[l][1]] == 0:
                    del mp[arr[l][1]]
                l += 1
        return res
