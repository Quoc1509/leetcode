class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        if k == 0:
            return [0] * len(code)
        N = len(code)
        code = code + code
        prefix = [0] * len(code)
        res = []
        prefix[0] = code[0]
        for i in range(1, len(code)):
            prefix[i] = prefix[i-1]+code[i]
        for i in range(abs(k), len(prefix)-1):
            res.append(prefix[i]-prefix[i-abs(k)])
        # print(res)
        return res[:N] if k > 0 else res[len(res)-N:]