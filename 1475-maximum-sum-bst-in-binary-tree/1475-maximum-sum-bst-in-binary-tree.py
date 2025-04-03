# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        def dfs(node):
            if not node:
                return inf, -inf, True, 0
            
            minLeft, maxLeft, isLeftValid, l = dfs(node.left)
            minRight, maxRight, isRightValid, r = dfs(node.right)

            if isLeftValid and isRightValid and maxLeft < node.val < minRight:
                res[0] = max(res[0], l+r+node.val)
                return min(minLeft, node.val), max(maxRight, node.val), True, l+r+node.val
            return 0, 0, False, -inf
        dfs(root)
        return res[0]