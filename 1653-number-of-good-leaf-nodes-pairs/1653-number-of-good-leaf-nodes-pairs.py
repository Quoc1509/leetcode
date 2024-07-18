# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = [0]
        def dfs(node):
            if not node: return []
            if not node.left and not node.right: return [1]
            left = dfs(node.left)
            right = dfs(node.right)
            # print(left,right)
            for i in range(len(left)):
                for j in range(len(right)):
                    if left[i] + right[j] <= distance: res[0] += 1
            temp = left+right
            return [s+1 for s in temp]
        dfs(root)
        return res[0]
