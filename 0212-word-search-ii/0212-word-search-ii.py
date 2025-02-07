class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        words = set(words)
        M, N = len(board), len(board[0])
        surround = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = set()
        trie = {}
        for word in words:
            temp = trie
            for s in word:
                if s not in temp:
                    temp[s] = {}
                temp = temp[s]
            temp['target'] = word

        def backTracking(r, c, tree):
            if 'target' in tree:
                res.add(tree['target'])
            temp = board[r][c]
            board[r][c] = '.'
            for x, y in surround:
                ro, co = r+x, c+y
                if 0 <= ro < M and 0 <= co < N and board[ro][co] in tree and board[ro][co] != '.':
                    backTracking(ro, co, tree[board[ro][co]])
            board[r][c] = temp

        for i in range(M):
            for j in range(N):
                if board[i][j] in trie:
                    backTracking(i, j, trie[board[i][j]])        
        return list(res)