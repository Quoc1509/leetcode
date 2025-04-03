# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # pre = ListNode(0, head)
        cur = pre = head
        while cur and cur.next:
            cur = cur.next.next
            pre = pre.next

        # if cur:
        #     temp = pre
        #     temp.next = None
        #     pre = pre.next

        p = None
        while pre:
            temp = pre.next
            pre.next = p
            p = pre
            pre = temp
        
        while head and p:
            if head.val != p.val:
                return False
            head = head.next
            p = p.next

        return True

        
            

        