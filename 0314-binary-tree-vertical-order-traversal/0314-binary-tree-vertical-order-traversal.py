# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        mp = defaultdict(list)
        q = deque()
        q.append((root, 0))
        index = deque([0])
        while q:
            for _ in range(len(q)):
                node, i = q.popleft()
                if i > index[-1]:
                    index.append(i)
                if i < index[0]:
                    index.appendleft(i)
                mp[i].append(node.val)
                if node.left:
                    q.append((node.left, i-1))
                if node.right:
                    q.append((node.right, i+1))
        res = []
        for i in index:
            res.append(mp[i])
        return res