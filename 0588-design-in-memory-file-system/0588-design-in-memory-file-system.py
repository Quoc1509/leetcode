class FileSystem:

    def __init__(self):
        self.trie = {}

    def ls(self, path: str) -> List[str]:
        folder = path.split('/')
        cur = self.trie
        res = []
        for s in folder:
            if s not in cur:
                break
            pre = cur
            cur = cur[s]
        if cur and '*'+folder[-1] in cur:
            return [folder[-1]]
        for key in cur.keys():
            if key[0] == '*':
                key = key[1:]
            res.append(key)
        res.sort()
        return res

    def mkdir(self, path: str) -> None:
        folder = path.split("/")
        cur = self.trie
        for s in folder:
            if s not in cur:
                cur[s] = {}
            cur = cur[s]

    def addContentToFile(self, filePath: str, content: str) -> None:
        folder = filePath.split("/")
        fileName = folder.pop()
        cur = self.trie
        for s in folder:
            if s not in cur:
                cur[s] = {}
            cur = cur[s]
        fileName = '*'+fileName
        if fileName not in cur:
            cur[fileName] = content
        else:
            cur[fileName] += content

    def readContentFromFile(self, filePath: str) -> str:
        folder = filePath.split("/")
        fileName = folder.pop()
        cur = self.trie
        res = ''
        for s in folder:
            if s not in cur:
                break
            cur = cur[s]
        fileName = '*'+fileName
        if fileName in cur:
            res = cur[fileName]
        return res

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)