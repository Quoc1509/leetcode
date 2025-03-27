# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        extra = 0
        cur = head = ListNode(inf, None)

        def addMore(node2, n):
            nonlocal cur
            new_extra = n
            while node2:
                num = (node2.val+new_extra) % 10
                new_extra = (node2.val+new_extra) // 10
                cur.next = ListNode(num, None)
                cur = cur.next
                node2 = node2.next
            return new_extra
            

        while cur1 and cur2:
            num = (cur1.val+cur2.val+extra) % 10
            extra = (cur1.val+cur2.val+extra) // 10
            cur.next = ListNode(num, None)
            cur1 = cur1.next
            cur2 = cur2.next
            cur = cur.next
        if cur1:
            extra = addMore(cur1, extra)
        if cur2:
            extra = addMore(cur2, extra)
        if extra:
            cur.next = ListNode(extra, None)
        return head.next
        