class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class DoubleList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    

    def remove(self):
        node = self.head.next
        temp = self.head.next.next
        self.head.next = temp
        temp.prev = self.head
        return node

    def add(self, node):
        temp = self.head.next

        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node

    def remove_node(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p
    
    def top(self):
        return self.head.next.val

    def print(self):
        cur = self.head.next
        print('----------------')
        while cur != self.tail:
            
            print(cur.val)
            cur = cur.next

class MaxStack:

    def __init__(self):
        self.maxStack = SortedList()
        self.mp = defaultdict(list)
        self.stack = DoubleList()

    def push(self, x: int) -> None:
        self.maxStack.add(x)
        node = Node(x)
        self.mp[x].append(node)
        self.stack.add(node)


    def pop(self) -> int:
        node = self.stack.remove()
        self.maxStack.remove(node.val)
        self.mp[node.val].pop()
        if not self.mp[node.val]:
            del self.mp[node.val]
        return node.val
        
    def top(self) -> int:
        self.stack.print()
        return self.stack.top()

    def peekMax(self) -> int:
        return self.maxStack[-1]

    def popMax(self) -> int:
        num = self.maxStack.pop()
        node = self.mp[num].pop()
        if not self.mp[num]:
            del self.mp[num]
        self.stack.remove_node(node)
        return num

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()