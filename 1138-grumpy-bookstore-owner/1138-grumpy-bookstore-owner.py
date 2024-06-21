class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        sum1, sum2 = 0, 0
        temp = 0
        for i in range(minutes):
            if grumpy[i] == 0:
                sum1 += customers[i]
            else:
                temp += customers[i]
        sum2 = temp
        l= 0
        for r in range(minutes, len(customers)):
            if grumpy[r] == 0:
                sum1 += customers[r]
            else:
                temp += customers[r]
            if grumpy[l] == 1:
                temp -= customers[l]
            sum2 = max(sum2, temp)
            l += 1
        # print(sum1, sum2)
        return sum1+sum2

            