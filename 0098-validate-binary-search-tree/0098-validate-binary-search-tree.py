# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(cur):
            if not cur:
                return inf, -inf, True
            
            mLL, mRL, l = dfs(cur.left) 
            mLR, mRR, r = dfs(cur.right)
            if l and r and mRL < cur.val < mLR:
                return min(mLL, cur.val), max(mRR, cur.val), True
            return 0, 0, False 
        
        a,b,c = dfs(root)
        return c