# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        count = 0
        cur = head
        res = None
        def reverse(start, end):
            node = start
            pre = None
            while node != end:
                ne = node.next
                node.next = pre
                pre = node
                node = ne
            return pre, start

        while cur:
            count += 1
            cur = cur.next
            if count == k:
                s, e = reverse(dummy.next, cur)
                if res == None:
                    res = s
                
                dummy.next = s
                e.next = cur
                dummy = e
                count = 0
        return res

        