class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for i in range(1, len(asteroids)):
            stack.append(asteroids[i])
            while len(stack) > 1 and stack[-2] > 0 and stack[-1] < 0:
                left = stack.pop()
                right = stack.pop()
                if right < abs(left):
                    stack.append(left)
                elif right > abs(left):
                    stack.append(right)
                else:
                    break  
        return stack