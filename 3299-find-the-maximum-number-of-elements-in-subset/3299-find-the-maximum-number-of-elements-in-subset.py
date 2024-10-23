class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = count[1] if count[1] % 2 == 1 else count[1]-1
        vis = defaultdict(int)
        for key, item in count.items():
            if key == 1 or vis[key] > 0:
                continue
            x = key
            temp = 0

            while vis[x] == 0 and count[x] >= 2:
                vis[x] = 1
                temp += 1
                x *= x
                
            if count[x] >= 2:
                vis[key] = temp + vis[x]
            else:
                vis[key] = temp + count[x]
                
            res = max(res, vis[key] + vis[key] - 1)
        return res