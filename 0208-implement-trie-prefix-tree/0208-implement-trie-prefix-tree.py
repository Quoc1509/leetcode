class Node:
    def __init__(self):
        self.prefix = {}
        self.val = False

class Trie:

    def __init__(self):
        self.obj = Node()

    def insert(self, word: str) -> None:
        temp = self.obj
        for i in word:
            if i not in temp.prefix:
                temp.prefix[i] = Node()
            temp = temp.prefix[i]
        temp.val = True


    def search(self, word: str) -> bool:
        temp = self.obj
        for i in word:
            if i not in temp.prefix:
                return False
            temp = temp.prefix[i]
        return temp.val

    def startsWith(self, prefix: str) -> bool:
        temp = self.obj
        for i in prefix:
            if i not in temp.prefix:
                return False
            temp = temp.prefix[i]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)