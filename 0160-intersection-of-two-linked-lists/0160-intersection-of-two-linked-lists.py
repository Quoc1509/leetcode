# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1 = headA
        l2 = headB
        cnt1 = cnt2 = 0
        while cnt1 < 2 and cnt2 < 2:
            if not l1:
                l1 = headB
                cnt1 += 1
            if not l2:
                l2 = headA
                cnt2 += 1
            if l1 == l2:
                return l1
            l1 = l1.next
            l2 = l2.next
        return None