# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def check(n, l):
            if not l: return True
            if not n or n.val != l.val:
                return False
            
            return check(n.left, l.next) or check(n.right, l.next)

        def dfs(node, head):
            if not node: return False
            if node.val == head.val:
                if check(node, head):
                    return True
            return dfs(node.left, head) or dfs(node.right, head)
        
        return dfs(root, head)
