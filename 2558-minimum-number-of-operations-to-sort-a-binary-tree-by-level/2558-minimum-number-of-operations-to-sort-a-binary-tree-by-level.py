# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        q = deque()
        q.append(root)
        arr = []
        res = [0]
        def check(ar):
            temp = {}
            for i, e in enumerate(ar):
                temp[e] = i
            correct = sorted(ar)

            for i in range(len(ar)):
                if ar[i] != correct[i]:
                    res[0] += 1
                    index = temp[correct[i]]
                    temp[ar[i]] = temp[correct[i]]
                    ar[index] = ar[i] 
        while q:
            check(arr)
            arr = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    arr.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    arr.append(node.right.val)
        return res[0]