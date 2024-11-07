# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        count = 0
        cur = head
        first, second = None, None
        while cur:
            count += 1
            if count == k:
                first = cur
            if count == length-k+1:
                second = cur
            cur = cur.next
        first.val, second.val = second.val, first.val
        return head
            