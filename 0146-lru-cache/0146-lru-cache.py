class LinkedList:
    def __init__(self, key=0, value=0, pre_node=None, next_node=None):
        self.key = key
        self.value = value
        self.prev = pre_node
        self.next = next_node


class LRUCache:
    def __init__(self, capacity: int):
        self.mp = {}
        self.capacity = capacity
        self.head = LinkedList(0, 0, None, None)
        self.tail = LinkedList(0, 0, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head


    def add_node(self, node):
        p = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        p.next = node
        node.prev = p

    def connect_node(self, node):
        temp = node
        node.prev.next = temp.next
        node.next.prev = temp.prev

    def get(self, key: int) -> int:   
        if key not in self.mp:
            return -1

        node = self.mp[key]
        self.connect_node(node)
        self.add_node(node)

        return self.mp[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            node.value = value
            self.connect_node(node)
            self.add_node(node)
            return

        if len(self.mp) == self.capacity:
            node = self.head.next
            k = node.key
            self.connect_node(node)
            del self.mp[k]

        node = LinkedList(key, value, None, None)
        self.mp[key] = node
        self.add_node(node)
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)