class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = deque()
        for i in range(len(arr)):
            if len(res) < k:
                res.append(arr[i])
            else:
                if abs(x-res[0]) > abs(x-arr[i]):
                    res.popleft()
                    res.append(arr[i])
        return list(res)