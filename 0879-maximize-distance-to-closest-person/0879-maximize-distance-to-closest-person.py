class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        maxLeft = 0
        for i in range(len(seats)):
            if seats[i] == 1:
                break
            maxLeft += 1
        maxRight = 0
        for i in range(len(seats)-1, -1, -1):
            if seats[i] == 1:
                break
            maxRight += 1
        stack = []
        for i in range(len(seats)):
            if seats[i] == 1:
                stack.append(i)
        
        l = stack[0] if len(stack) > 1 else 0
        r = stack[1] if len(stack) > 1 else 0
        for i in range(len(stack)-1):
            if stack[i+1] - stack[i] > r-l:
                l, r = stack[i], stack[i+1]
        if maxLeft > maxRight and maxLeft > (r-l)//2:
            return maxLeft
        elif maxRight > maxLeft and maxRight > (r-l)//2:
            return maxRight
        else:
            return (r-l)// 2        
        