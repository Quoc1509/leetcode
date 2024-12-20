# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append(root) 
        level = 0
        def reverse(arr):
            N = len(arr)
            for i in range(N//2):
                arr[i].val, arr[N-i-1].val = arr[N-i-1].val, arr[i].val
        while q:
            if level % 2 == 1:
                reverse(q)
            for _ in range(len(q)):      
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return root