class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.mp = {}    
        self.head = Node(0, Node(homepage))
        self.cur = 0
        self.mp[self.cur] = self.head
        self.last = 1
    
    def addNode(self, cur, nextNode):
        cur.next = nextNode
        self.mp[self.cur] = cur

    def visit(self, url: str) -> None:
        newNode = Node(url)
        curNode = self.mp[self.cur].next
        self.cur += 1
        self.addNode(curNode, newNode)
        self.last = self.cur + 1

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.mp[self.cur].next.val

    def forward(self, steps: int) -> str:
        self.cur = min(self.cur+steps, self.last-1)
        return self.mp[self.cur].next.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)