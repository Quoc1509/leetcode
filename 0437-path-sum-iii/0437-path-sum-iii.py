# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pre_sum = defaultdict(int)
        pre_sum[0] = 1
        res = [0]
        def dfs(node, s):
            if not node: return
            s += node.val
            res[0] += pre_sum[s-targetSum]
            pre_sum[s] += 1
            dfs(node.left, s)
            dfs(node.right, s)
            pre_sum[s] -= 1

        dfs(root, 0)
        return res[0]
