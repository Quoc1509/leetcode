class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9+7
        stack = []
        res = 0
        arr.append(-inf)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                j = stack.pop()
                l = (stack[-1] if stack else -1) + 1
                r = i - 1
                res = (res + (r-j+1)*(j-l+1)*arr[j]) % mod
            stack.append(i)
        return res        