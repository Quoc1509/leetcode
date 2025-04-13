class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        temp = [s.split(":") for s in logs]
        for i in range(len(logs)):
            if not stack:
                stack.append(int(temp[i][0]))
            elif temp[i-1][1] == "start" and temp[i][1] == "end":
                res[stack[-1]] += int(temp[i][2]) - int(temp[i-1][2]) + 1
                stack.pop()
            elif temp[i-1][1] == "end" and temp[i][1] == "start":
                res[stack[-1]] += int(temp[i][2]) - int(temp[i-1][2]) - 1
                stack.append(int(temp[i][0]))
            elif temp[i-1][1] == "start" and temp[i][1] == "start":
                res[stack[-1]] += int(temp[i][2]) - int(temp[i-1][2])
                stack.append(int(temp[i][0]))
            elif temp[i-1][1] == "end" and temp[i][1] == "end":
                res[stack[-1]] += int(temp[i][2]) - int(temp[i-1][2])
                stack.pop()

        return res