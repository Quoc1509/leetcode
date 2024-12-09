class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        count = 0
        temp = [] 
        res = [True] * len(queries)
        if len(nums) < 2: return res
        for i in range(len(nums)-1):
            if (nums[i]%2==0 and nums[i+1]%2!=0) or (nums[i]%2!=0 and nums[i+1]%2==0):
                temp.append(count)
            else:
                
                temp.append(count)
                count += 1
        if(nums[-1]%2==0 and nums[-2]%2!=0) or (nums[-1]%2!=0 and nums[-2]%2==0):
            temp.append(count)
        else:
            temp.append(count+1)
        
        for i in range(len(queries)):
            a, b = queries[i]
            if temp[a] != temp[b]:
                res[i] = False
        # print(res)
        return res