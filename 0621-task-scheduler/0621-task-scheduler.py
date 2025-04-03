class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        # heap = []
        # for key, item in count.items():
        #     heappush(heap, -item)
        # res = 0
        # while heap:
        #     temp = []
        #     count = 0
        #     cycle = n + 1
        #     while heap and cycle > 0:
        #         num = heappop(heap)
        #         num += 1
        #         if num < 0:
        #             temp.append(num)
        #         count += 1
        #         cycle -= 1

            
            
        #     for number in temp:
        #         heappush(heap, number) 

        #     res += count if cycle == 0 or not heap else (n+1)
        # return res

        arr = sorted(count.values(), reverse=True)
        idle = (arr[0]-1) * (n)
        print(idle)
        for i in range(1, len(arr)):
            idle -= min(arr[0]-1, arr[i])
        print(idle)
        return len(tasks) + max(0, idle)