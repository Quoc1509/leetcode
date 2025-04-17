"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        q = deque([root])
        while q:
            node = None
            for _ in range(len(q)):
                n = q.popleft()
                if not node:
                    node = n
                else:
                    node.next = n
                    node = node.next
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return root