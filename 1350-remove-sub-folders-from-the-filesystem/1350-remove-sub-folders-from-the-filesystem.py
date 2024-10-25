class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        trie = {}
        
        res = []
        for s in folder:
            temp = s.split('/')
            check = True
            cur = trie
            for e in temp:
                if e not in cur:
                    cur[e] = {}
                cur = cur[e]
                if 1 in cur:
                    check = False
                    break
            if check:
                cur[1] = 1
                res.append(s)
        return res