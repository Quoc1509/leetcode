class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        N = len(searchWord)
        words = sentence.split()
        for i in range(len(words)):
            if words[i][:N] == searchWord:
                return i+1
        return -1