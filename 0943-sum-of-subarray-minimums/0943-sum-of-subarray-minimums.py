class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        stack = []
        arr.append(-inf)
        for i in range(len(arr)):
            left, right = 0, 0
            while stack and arr[stack[-1]] >= arr[i]:
                index = stack.pop()
                res += (index-(stack[-1] if stack else -1)) * (i-index) * arr[index]
            stack.append(i)

        return res % (10**9+7)
        