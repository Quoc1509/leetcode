class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        surfix = [0] * len(boxes)
        one = 0 if boxes[-1] == '0' else 1
        for i in range(len(surfix)-2, -1, -1):
            surfix[i] += (surfix[i+1]+one)
            if boxes[i] == '1':
                one += 1
        prefix = [0] * len(boxes)
        one = 0 if boxes[0] == '0' else 1
        for i in range(1, len(boxes)):
            prefix[i] += (prefix[i-1]+one)
            if boxes[i] == '1':
                one += 1
        res = []
        for i in range(len(boxes)):
            res.append(prefix[i]+surfix[i])
        return res