# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = [0]
        def dfs(node, nums):
            nums = (nums*10+node.val)
            if not node.left and not node.right:
                res[0] += nums
            
            if node.left:
                dfs(node.left, nums)
            if node.right:
                dfs(node.right, nums)
        dfs(root, 0)
        return res[0]