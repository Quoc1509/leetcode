# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        
        q = deque()
        q.append(root)
        while q:
            maxCur = 0
            for _ in range(len(q)):
                node = q.popleft()
                maxCur += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(maxCur)
        res.sort(reverse=True)
        if len(res) < k:
            return -1
        return res[k-1]