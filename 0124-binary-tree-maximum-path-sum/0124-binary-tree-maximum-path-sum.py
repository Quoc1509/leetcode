# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [-inf]
        
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            total = left + right
            
            if total < 0:

                res[0] = max(res[0], max(left, right, 0) + node.val)
                return max(left, right, 0) + node.val
            elif left < 0:
                # print(node.val, left, right)
                res[0] = max(res[0], right+node.val)
                return right+node.val
            elif right < 0:
                
                res[0] = max(res[0], left+node.val)
                return left+node.val
            res[0] = max(res[0], total+node.val)
            return max(left, right) + node.val

        dfs(root)
        return res[0]