# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0, 0
            countL, sumL = dfs(node.left)
            countR, sumR = dfs(node.right)
            
            total = sumL+sumR+node.val
            count = countL+countR+1
            if total // count == node.val:
                res += 1
            return count, total
        dfs(root)
        return res