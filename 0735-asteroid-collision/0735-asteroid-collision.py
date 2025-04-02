class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        noCollision = []
        for i in asteroids:
            noCollision.append(i)
            while len(noCollision) > 1 and noCollision[-1] < 0 and noCollision[-2] > 0:
                firstLast = noCollision.pop()
                secondLast = noCollision.pop()               
                if firstLast*(-1) > secondLast:
                    noCollision.append(firstLast)
                elif firstLast*(-1) < secondLast:
                    noCollision.append(secondLast)
                else:
                    break
        return noCollision

