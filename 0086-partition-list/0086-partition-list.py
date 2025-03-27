# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy1 = less = ListNode(0, None)
        dummy2 = great = ListNode(0, None)
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                great.next = head
                great = great.next
            head = head.next
        
        less.next = dummy2.next
        great.next = None
        return dummy1.next
        