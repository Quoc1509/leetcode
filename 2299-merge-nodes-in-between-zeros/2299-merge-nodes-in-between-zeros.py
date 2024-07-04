# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, temp = None, None
        a = 0
        while head:
            if head.val == 0:
                if not node: 
                    node = ListNode(a, None)
                    temp = node
                else: 
                    temp.next = ListNode(a, None)
                    temp = temp.next
                a = 0
            a += head.val
            head = head.next
                
        return node.next      
        
            