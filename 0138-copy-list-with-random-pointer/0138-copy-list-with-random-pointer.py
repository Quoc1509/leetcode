"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        cur = head
        while cur:
            new_node = Node(cur.val, cur.next, None)
            cur.next = new_node
            cur = new_node.next

        cur = head
        copy = head.next
        
        while cur:
            if cur.random:
                copy.random = cur.random.next
            cur = copy.next
            if cur:
                copy = cur.next
        
        res = head.next
        copy = res
        while copy and copy.next:
            copy.next = copy.next.next
            copy = copy.next
        return res

        