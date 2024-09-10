# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur.next:
            gcd = math.gcd(cur.val, cur.next.val)
            # print(gcd)
            node = ListNode(gcd, cur.next)
            cur.next = node
            cur = cur.next.next
        return head