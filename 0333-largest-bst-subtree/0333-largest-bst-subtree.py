# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return inf, -inf, 0, True
            mLL, mRL, l, validLeft = dfs(node.left)
            mLR, mRR, r, validRight = dfs(node.right)

            if validLeft and validRight and node.val > mRL and node.val < mLR:
                return min(mLL, node.val), max(mRR, node.val), l+r+1, True
            return 0, 0, max(l, r), False
        a,b,c,d = dfs(root)
        return c