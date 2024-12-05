class Solution:
    def canChange(self, start: str, target: str) -> bool:
        S, T = len(start), len(target)
        s_index, t_index = 0, 0
        while s_index < S or t_index < T:
            while s_index < S and start[s_index] == '_':
                s_index += 1
            while t_index < T and target[t_index] == '_':
                t_index += 1
            if t_index == len(target) or s_index == len(start):
                break
            if start[s_index] != target[t_index] or (target[t_index] == 'L' and t_index > s_index) or (target[t_index] == 'R' and t_index < s_index):
                return False
            s_index += 1
            t_index += 1
        # print(s_index, t_index)
        return s_index == t_index
        