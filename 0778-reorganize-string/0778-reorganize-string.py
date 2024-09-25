class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [(-item, key) for key, item in count.items()]
        heapify(heap)
        res = ''
        while len(heap) > 1:
            num1, alpha1 = heappop(heap)
            num2, alpha2 = heappop(heap)
            res += alpha1 + alpha2
            num1 += 1
            num2 += 1
            if num1 != 0:
                heappush(heap, (num1, alpha1))
            if num2 != 0:
                heappush(heap, (num2, alpha2))
        if not heap: 
            return res
        if (res and res[-1] == heap[0][1]) or heap[0][0] < -1:
            return ''
        return res+heap[0][1]