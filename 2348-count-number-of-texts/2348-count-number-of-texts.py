class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        N = len(pressedKeys)
        CONS = (10**9)+7
        @cache
        def dfs(i):
            if i >= N:
                return 1
            count = dfs(i+1)
            if i < N-1 and pressedKeys[i] == pressedKeys[i+1]:
                count += dfs(i+2)
            if i < N-2  and pressedKeys[i] == pressedKeys[i+1] == pressedKeys[i+2]:
                count += dfs(i+3)
            if pressedKeys[i] == '7' or pressedKeys[i] == '9': 
                if i < N-3 and pressedKeys[i] == pressedKeys[i+1] == pressedKeys[i+2] == pressedKeys[i+3]:
                    count += dfs(i+4)
            return count % CONS
        return dfs(0) 
        