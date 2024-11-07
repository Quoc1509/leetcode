class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = {}
        res = 0
        for num in nums:
            bit = bin(num)[2:]
            bit = ('0' * (33-len(bit)))+ bit
            cur = trie
            path = ''
            for i in bit:
                if i not in cur:                    
                    cur[i] = {}
                cur = cur[i]
                
            cur = trie
            for i in bit:
                if i == '1':
                    if '0' in cur:
                        cur = cur['0']
                        path += '1'
                    else:
                        cur = cur['1']
                        path += '0'
                else:
                    if '1' in cur:
                        cur = cur['1']
                        path += '1'
                    else:
                        cur = cur['0']
                        path += '0'
            res = max(res, int(path, 2))
        return res