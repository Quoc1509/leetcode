P = [True] * 1001
for i in range(2, int(1001*0.5)+1):
    if P[i]:
        for j in range(i*i, 1001, i):
            P[j] = False
A = []
for i in range(2, 1001):
    if P[i]:
        A.append(i)

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:    

        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= nums[i+1]:
                temp = -1
                for j in A:
                    if nums[i]-j < nums[i+1]:
                        temp = nums[i]-j
                        break
                if temp <= 0:
                    return False
                nums[i] = temp
        # print(nums)
        return True