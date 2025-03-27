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

        mp = {}
        cur = head
        dummy = pre = Node(0, None, None)
        while cur:
            temp = Node(cur.val, None, None)
            mp[cur] = temp
            pre.next = temp
            pre = pre.next
            cur = cur.next

        cur1 = head
        cur2 = dummy.next
        while cur1:
            if cur1.random:
                cur2.random = mp[cur1.random]
            cur1 = cur1.next
            cur2 = cur2.next
        return dummy.next
            
            
        