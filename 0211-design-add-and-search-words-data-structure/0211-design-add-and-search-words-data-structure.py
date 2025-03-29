class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        tree = self.trie
        for c in word:
            if c not in tree:
                tree[c] = {}
            tree = tree[c]
        tree['end'] = True

    def search(self, word: str) -> bool:
        return self.dfs(word, 0, self.trie)

    def dfs(self, word, i, tree):
        if i == len(word):
            print(tree)
            return 'end' in tree
        
        if word[i] == '.':
            for key, item in tree.items():
    
                if key != 'end' and self.dfs(word, i+1, item):
                    return True
            return False
        elif word[i] not in tree:
            return False

        return self.dfs(word, i+1, tree[word[i]])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)