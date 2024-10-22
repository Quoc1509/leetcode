class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        surfix = [0] * (len(boxes)+1)
        res = [0] * len(boxes)
        one = 0
        for i in range(len(boxes)-1, -1, -1):
            surfix[i] = one + surfix[i+1] 
            if boxes[i] == '1':
                one += 1
        one = 0
        prefix = 0
        for i in range(len(res)):
            res[i] = prefix + surfix[i]
            if boxes[i] == '1':
                one += 1
            prefix += one
        return res