class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        res, l = 0, 0
        minQ, maxQ = deque(), deque()
        for i in range(len(nums)):     
            while maxQ and nums[maxQ[-1]] < nums[i]:
                maxQ.pop()
            while minQ and nums[minQ[-1]] > nums[i]:
                minQ.pop()

            maxQ.append(i)
            minQ.append(i)   
            # print(minQ, maxQ)
            while nums[maxQ[0]]-nums[minQ[0]] > 2:
                if minQ[0] < maxQ[0]:
                    l = minQ.popleft()
                elif minQ[0] > maxQ[0]:
                    l = maxQ.popleft()
                l += 1
            
            res += (i-l+1)

        return res
            
