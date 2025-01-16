class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        T = {}
        for word in products:
            temp = T
            for c in word:
                if c not in temp:
                    temp[c] = {}
                temp = temp[c] 
                if not 'word' in temp:
                    temp['word'] = []
                if len(temp['word']) < 3:
                    temp['word'].append(word)
        cur = T
        res = []
        for c in searchWord:
            if c not in cur:
                res.append([])
                cur[c] = {}
                cur = cur[c]
            else:
                cur = cur[c]
                res.append(cur['word'])
        # print(res)
        return res