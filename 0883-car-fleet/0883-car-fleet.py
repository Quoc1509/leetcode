class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        for a, b in zip(position, speed):
            pair.append((a, b))
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            t = (target-p)/s
            if stack:
                if t <= stack[-1]:
                    continue
            stack.append(t)
        return len(stack)
