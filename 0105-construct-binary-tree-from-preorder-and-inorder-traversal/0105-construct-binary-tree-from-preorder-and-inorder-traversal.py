# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = {}
        for i, e in enumerate(inorder):
            mp[e] = i
        pre_index = 0
        def dfs(in_start, in_end):
            nonlocal pre_index
            if in_start > in_end:
                return None
            node = TreeNode(preorder[pre_index])
            mid = mp[preorder[pre_index]]
            pre_index += 1
            node.left = dfs(in_start, mid-1)
            node.right = dfs(mid+1, in_end)
            return node
        return dfs(0, len(inorder)-1)