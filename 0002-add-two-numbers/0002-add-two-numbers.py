# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        extra = 0
        cur1 = l1
        cur2 = l2
        cur = head = None

        def addMore(h, c, temp, e):
            x = e
            while temp:
                n = (temp.val+x)%10
                x = (temp.val+x)//10
                c.next = ListNode(n, None)
                c = c.next
                temp = temp.next
            if x != 0:
                c.next = ListNode(x, None)
            return h

        while cur1 and cur2:
            num = (cur1.val+cur2.val+extra) % 10
            extra = (cur1.val+cur2.val+extra) // 10      
            if not head:
                head = ListNode(num, None)
                cur = head
            else:
                cur.next = ListNode(num, None)
                cur = cur.next
            cur1 = cur1.next
            cur2 = cur2.next
        if extra and not cur1 and not cur2:
            cur.next = ListNode(extra, None)
        if cur1:
            head = addMore(head, cur, cur1, extra)
        if cur2:
            head = addMore(head, cur, cur2, extra)
        return head