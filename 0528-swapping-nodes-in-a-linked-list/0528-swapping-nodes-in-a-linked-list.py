# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next:
            return head
        first, second = None, None
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        cur = head
        i = 0
        while cur:
            if i == k-1:
                first = cur
            if i == length-k:
                second = cur
            cur = cur.next
            i += 1
        first.val, second.val = second.val, first.val
        return head
            