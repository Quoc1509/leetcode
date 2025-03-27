class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        # get the largest potential outlier
        # elm1, elm2, ... elmn, sum(elm1..elmn), outlier
        # total sum = special sum x 2 + outlier
        # outlier = total sum - special sum x 2

        # get the counter of nums
        # for each num, treat it as the special sum
        # then outlier value is total sum - special sum x 2, if this outlier exists

        if not nums or len(nums) < 2:
            raise ValueError("no valid outlier")
        
        counter = Counter(nums)
        total_sum = sum(nums)
        res = -float('inf')

        for num in counter.keys():
            potential_outlier = total_sum - num * 2

            if potential_outlier in counter:
                if potential_outlier != num or counter[num] > 1:
                    res = max(res, potential_outlier)
        
        return res
        
         # O(n^2)
        # get the sum of all nums minue any 2 elements
        # get a list of tuples, each tuple is a tuple of ((elm1, elm2), sum)
        # for the above list
        #  - if elm1 == sum then elm2 is outlier
        #  - if elm2 == sum then elm1 is outlier
        # get the largest outlier
       
        # sum_of_nums = sum(nums)
        # res = -float('inf')
        # visited = set()
        
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if frozenset((nums[i], nums[j])) in visited:
        #             continue
        #         total = sum_of_nums - nums[i] - nums[j]
        #         visited.add(frozenset((nums[i], nums[j])))
        #         if nums[i] == total:
        #             res = max(res, nums[j])
        #         if nums[j] == total:
        #             res = max(res, nums[i])

        return res