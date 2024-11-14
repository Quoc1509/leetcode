# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        res = []
        @cache
        def dfs1(node):
            if not node: return -1
            l = dfs1(node.left)
            r = dfs1(node.right)
            return max(l, r) + 1

        dic = {}
        def dfs2(node, d, maxBranch):       
            if not node: return
            dic[node.val] = maxBranch  
            dfs2(node.left, d+1, max(maxBranch, d+1+dfs1(node.right)))
            dfs2(node.right, d+1, max(maxBranch, d+1+dfs1(node.left)))
        dfs1(root)
        dfs2(root, 0, 0)
        for q in queries:
            res.append(dic[q])
        return res