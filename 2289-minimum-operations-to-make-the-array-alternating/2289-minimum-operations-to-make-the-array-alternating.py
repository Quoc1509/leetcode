class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        even = defaultdict(int)
        odd = defaultdict(int)
        for i in range(len(nums)):
            if i % 2 == 0:
                even[nums[i]] += 1
            else:
                odd[nums[i]] += 1
        
        e = sorted([(item, key) for key, item in even.items()], reverse=True)
        o = sorted([(item, key) for key, item in odd.items()], reverse=True)
        lene = len(nums)//2 + (1 if len(nums) % 2 == 1 else 0)
        leno = len(nums)//2 

        if e[0][1] != o[0][1]:
            return lene-e[0][0] + leno-o[0][0]
        else:
            return min((lene-e[0][0] + leno- (o[1][0] if len(o) > 1 else 0)), (lene-(e[1][0] if len(e) > 1 else 0) + leno-o[0][0]))
    