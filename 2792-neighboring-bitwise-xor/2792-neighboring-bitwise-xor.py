class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # if len(derived) < 2:
        #     return False
        first = [1]
        second = [0]
        # if len()
        # if derived[0] == 0:
        #     first.append(1)
        #     second.append(0)
        # else:
        #     first.append(0)
        #     second.append(1)
        for i in range(len(derived)-1):
            first.append(derived[i]^first[-1])
            second.append(derived[i]^second[-1])
        if first[0]^first[-1] == derived[-1] or second[0]^second[-1]==derived[-1]:
            return True

        return False
