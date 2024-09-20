# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque()
        q.append(root)
        direct = 0
        res = []
        while q:
            temp = []
            nodes = deque()
            for _ in range(len(q)):
                cur = q.popleft()
                temp.append(cur.val)
                nodes.append(cur)
            
            res.append(temp[:])

            while nodes:
                n = nodes.pop()
                if direct % 2 != 0:
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
                else:
                
                    if n.right:
                        q.append(n.right)
                    if n.left:
                        q.append(n.left)    
            direct += 1
            
        return res
