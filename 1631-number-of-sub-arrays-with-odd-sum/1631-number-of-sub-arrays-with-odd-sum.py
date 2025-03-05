class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # mp = defaultdict(int)
        # mp[0] = 1
        # total, res = 0, 0

        # for num in arr:
        #     total += num
        #     res += mp[1-(total%2)]
        #     mp[total%2] += 1
 
        # return res % (10**9+7)

        N = 10**9+7
        #dpOdd[i]: num of sub arrays have oddsum end at index i
        #dpEven[i]: num of sub arrays have evensum end at index i

        # dpOdd = [0] * (len(arr)+1)
        # dpEven = [0] * (len(arr)+1)
        # for i in range(len(arr)):
        #     if arr[i] % 2 == 0:
        #         dpOdd[i+1] = dpOdd[i]
        #         dpEven[i+1] = dpEven[i] + 1
        #     else:
        #         dpOdd[i+1] = dpEven[i] + 1
        #         dpEven[i+1] = dpOdd[i]  
        # return sum(dpOdd)%N

        dpOdd = 0
        dpEven = 0
        res = 0
        for num in arr:
            if num % 2 == 0:
                dpEven += 1
            else:
                newdpOdd = dpEven + 1
                dpEven = dpOdd
                dpOdd = newdpOdd
            res += dpOdd
        return res % N
            



