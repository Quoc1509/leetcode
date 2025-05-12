class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        even = []
        count = Counter(digits)
        for key in count.keys():
            if key % 2 == 0:
                even.append(key)
        keys = list(count.keys())
        keys.sort()
        even.sort()
        for i in range(len(keys)):
            if keys[i] == 0:
                continue
            temp1 = keys[i] * 100
            count[keys[i]] -= 1
            for j in range(len(keys)):
                if count[keys[j]] == 0:
                    continue
                temp2 = temp1 + (keys[j] * 10)
                count[keys[j]] -= 1
                for e in even:
                    if count[e] == 0:
                        continue
                    res.append(temp2 + e)
                count[keys[j]] += 1
            count[keys[i]] += 1
        return res

            