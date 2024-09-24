class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfNode = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, val):
        cur = self.root        
        for c in val:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfNode = True

    def search(self, val):
        count = 0
        cur = self.root
        for c in val:
            if c not in cur.children:
                break
            count += 1
            cur = cur.children[c]
        return count

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for num in arr1:
            trie.insert(str(num))
        res = 0
        for num in arr2:
            count = trie.search(str(num))
            res = max(res, count)
        return res