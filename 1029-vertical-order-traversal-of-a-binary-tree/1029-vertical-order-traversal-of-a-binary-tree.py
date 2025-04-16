# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        mp = defaultdict(list)

        def dfs(node, row, col):
            if not node:
                return

            mp[col].append((row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        dfs(root, 0, 0)
        res = [[] for _ in range(len(mp))]
        key = sorted(list(mp.keys()))
        i = 0

        for k in key:
            for a, b in sorted(mp[k]):
                res[i].append(b)
            i += 1
        return res