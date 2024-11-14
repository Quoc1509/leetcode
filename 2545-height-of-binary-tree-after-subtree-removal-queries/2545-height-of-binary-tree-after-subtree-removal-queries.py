# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        dp = defaultdict(int)
        dp[-1] = -1
        index = defaultdict(list)
        res = [0] * len(queries)
        for i, e in enumerate(queries):
            index[e].append(i)

        def dfs1(node):
            l = r = 0
            if node.left:
                l = dfs1(node.left)
            if node.right:
                r = dfs1(node.right)
            dp[node.val] = max(l, r)
            return max(l, r) + 1


        def update(ind, numB):
            for i in index[ind]:
                res[i] = numB
            del index[ind]



        def dfs2(node, d, maxBranch): 
            
            if not node: return
            if node.left:
                temp = max(maxBranch, d+1+dp[node.right.val if node.right else -1])
                if node.left.val in index:
                    update(node.left.val, temp)
                dfs2(node.left, d+1, temp)
            if node.right:
                temp = max(maxBranch, d+1+dp[node.left.val if node.left else -1])
                if node.right.val in index:
                    update(node.right.val, temp)
                dfs2(node.right, d+1, temp)
        dfs1(root)
        dfs2(root, 0, 0)
        return res