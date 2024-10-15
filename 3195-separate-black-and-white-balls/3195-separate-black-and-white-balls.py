class Solution:
    def minimumSteps(self, s: str) -> int:
        black = deque()
        for i, e in enumerate(s):
            if e == '1':
                black.append(i)
        index = len(s)-1
        count = 0
        while black:
            if s[index] == '1':
                black.pop()
            else:
                i = black.popleft()
                count += index - i
            index -= 1
        return count