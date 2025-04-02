class FileSystem:

    def __init__(self):
        self.trie = {}

    def createPath(self, path: str, value: int) -> bool:
        if not path or path == "/":
            return False
        pa = path.split("/")[1:]
        tree = self.trie
        for i in range(len(pa)-1):
            if pa[i] not in tree:
                return False
            tree = tree[pa[i]]

        if pa[-1] in tree:
            return False
        tree[pa[-1]] = {}
                
        tree = tree[pa[-1]]
        
        tree['content'] = value
        return True

    def get(self, path: str) -> int:
        if not path or path == "/":
            return -1
        pa = path.split("/")[1:]
        tree = self.trie
        for i in range(len(pa)):
            if pa[i] not in tree:
                return -1
            tree = tree[pa[i]]
        if 'content' in tree:
            return tree['content']
        return -1

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)