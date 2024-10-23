# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        q = deque()
        q.append(root)
        total = 0
        while q:
            temp = 0
            for i in range(len(q)):
                num = 0
                node = q.popleft()
                num += node.left.val if node.left else 0
                num += node.right.val if node.right else 0
                node.val = total - node.val
                if node.left:
                    node.left.val = num
                    q.append(node.left)
                if node.right:
                    node.right.val = num
                    q.append(node.right)
                temp += num
            total = temp
        root.val = 0
        return root
                