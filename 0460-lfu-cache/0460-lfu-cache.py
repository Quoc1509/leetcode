class Node:
    def __init__(self, key=0, value=0, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next 

class DoubleList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_tail(self, node):
        pre_node = self.tail.prev
        pre_node.next = node
        node.prev = pre_node
        node.next = self.tail
        self.tail.prev = node

    def remove_node(self, node):
        p, n = node.prev, node.next
        p.next = node.next
        n.prev = node.prev

    def remove_head(self):
        key = self.head.next.key
        self.remove_node(self.head.next)
        return key
    
    def isEmpty(self):
        return self.head.next == self.tail

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = {} # key: [freq, node]
        self.freq_map = defaultdict(lambda: DoubleList())
        self.minFreq = 1
    
    def increaseFreq(self, key):
        f, node = self.mp[key]
        freq = self.freq_map[f]
        freq.remove_node(node)
        if freq.isEmpty():
            if self.minFreq == f:
                self.minFreq += 1

            del self.freq_map[f]

        f += 1
        self.freq_map[f].add_tail(node)
        self.mp[key] = [f, node]

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1

        self.increaseFreq(key)

        f, node = self.mp[key]

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            k, node = self.mp[key]
            node.value = value
            self.increaseFreq(key)
            return
        if len(self.mp) == self.capacity:
            f = self.minFreq
            freqList = self.freq_map[f]
            k = freqList.remove_head()
            if freqList.isEmpty():
                del self.freq_map[f]
            del self.mp[k]
        
        node = Node(key, value)
        self.minFreq = 1
        self.mp[key] = [1, node]
        freqList = self.freq_map[1]
        freqList.add_tail(node)

        
                


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)