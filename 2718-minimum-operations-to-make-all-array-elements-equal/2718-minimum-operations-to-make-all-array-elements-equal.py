class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        res = []
        nums.sort()
        pre = [0]*(len(nums)+1)
        for i in range(1, len(pre)):
            pre[i] = pre[i-1] + nums[i-1]

        for i in range(len(queries)):
            l, r = 0, len(nums)-1
            
            while l <= r:
                m = (l+r)//2
                if nums[m] < queries[i]:
                    l = m + 1
                else:
                    r = m - 1
    
            if l == len(nums):
                res.append(queries[i]*len(nums)-pre[-1])
            else:
                left = l
                right = len(nums)-l
                total = abs((queries[i]*left)-pre[left]) + abs(queries[i]*right-(pre[-1]-pre[left]))
                res.append(total)

        return res