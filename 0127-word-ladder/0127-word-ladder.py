import string 

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        alpha = string.ascii_lowercase
        if endWord not in wordList: return 0
        q = deque([beginWord])
        count = 1
        # visited = set()
        # visited.add(beginWord)
        while q:
            for _ in range(len(q)):
                word = q.popleft()  
                if word == endWord:
                    return count           
                for i in range(len(word)):
                    for w in alpha:
                        temp = word[:i] + w + word[i+1:]
                        if temp in wordList:
                            q.append(temp)
                            wordList.remove(temp)
                            # visited.add(temp)

            count += 1
        return 0
