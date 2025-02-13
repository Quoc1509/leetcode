class Node:
    def __init__(self):
        self.value = set()
        self.count = 1
        self.next = None
        self.prev = None
    
    
class AllOne:
    def __init__(self):
       self.map = {}
       self.head = Node()
       self.head.count = -inf
       self.tail = Node()
       self.tail.count = inf
       self.head.next = self.tail
       self.tail.prev = self.head
       
    def inc(self, key: str) -> None:
        if key not in self.map:
            if self.head.next.count == 1:
                self.head.next.value.add(key)
                self.map[key] = self.head.next
            else:
                new_node = Node()
                new_node.value.add(key)
                temp = self.head.next
                self.head.next = new_node
                new_node.next = temp
                temp.prev = new_node
                new_node.prev = self.head
                self.map[key] = new_node
        else:
            node = self.map[key]
            if node.count + 1 == node.next.count:
                node.next.value.add(key)
            else:
                new_node = Node()
                new_node.count = node.count+1
                new_node.value.add(key)
                temp = node.next
                node.next = new_node
                new_node.next = temp
                temp.prev = new_node
                new_node.prev = node
            node.value.remove(key)
            self.map[key] = node.next
            if len(node.value) == 0:
                node.prev.next = node.next
                node.next.prev = node.prev

    def dec(self, key: str) -> None:
        node = self.map[key]
        node.value.remove(key)
        if node.count == 1:
            del self.map[key]
            if len(node.value) == 0:
                node.next.prev = node.prev
                node.prev.next = node.next
        else:
            if node.prev.count == node.count - 1:
                node.prev.value.add(key)
                self.map[key] = node.prev
            else:
                new_node = Node()
                new_node.value.add(key)
                new_node.count = node.count-1
                temp = node.prev
                new_node.next = node
                node.prev = new_node
                new_node.prev = temp
                temp.next = new_node
                self.map[key] = new_node
            if len(node.value) == 0:
                node.next.prev = node.prev
                node.prev.next = node.next


    def getMaxKey(self) -> str:
        temp = self.tail.prev.value
        l = len(temp)
        if l == 0:
            return ''
        for elem in temp:
            return elem
        
    def getMinKey(self) -> str:
        temp = self.head.next.value
        l = len(temp)
        if l == 0:
            return ''
        for elem in temp:
            return elem
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()