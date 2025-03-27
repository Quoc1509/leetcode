import string 

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        alpha = string.ascii_lowercase
        res = 1
        q = deque()
        q.append(beginWord)
        visit = set()
        visit.add(beginWord)
        while q:
            for _ in range(len(q)):
                s = q.popleft()
                if s == endWord:
                    return res
                for i in range(len(s)):
                    
                    for c in alpha:
                        temp = s[:i] + c + s[i+1:]
                        # print(temp)
                        if temp not in visit and temp in wordList:
                            q.append(temp)
                            visit.add(temp)
            res += 1
        return 0