class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visit = defaultdict(int)
        for i in range(len(nums)):
            nums[i]
            if nums[i] in visit:
                return [visit[nums[i]], i]
            visit[target - nums[i]] = i
        return []