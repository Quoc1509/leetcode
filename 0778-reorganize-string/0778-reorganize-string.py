class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxF, maxC = 0, ''
        # heap = []
        for ch, fre in count.items():
            if fre > maxF:
                maxF = fre
                maxC = ch
            # heappush(heap, (-fre, ch))
        if maxF > (len(s)+1)//2:
            return ''
        # res = ''
        # while heap:
        #     count1, first = heappop(heap)
        #     res += first
        #     if heap:
        #         count2, second = heappop(heap)
        #         res += second
        #         count2 += 1
        #         if count2 < 0:
        #             heappush(heap, (count2, second))
        #     count1 += 1
        #     if count1 < 0:
        #         heappush(heap, (count1, first))
        # return res

        res = [''] * len(s)
        index = 0
        while count[maxC] > 0:
            res[index] = maxC
            count[maxC] -= 1
            index += 2
        
        for ch, freq in count.items():
            while freq > 0:
                if index >= len(s):
                    index = 1
                res[index] = ch
                index += 2
                freq -= 1
        return ''.join(res)