# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        res = None
        cur = head
        count = 0
        
        def reverse(start, end):
            k = prev = start
            start = None
            while prev != end:
                n = prev.next
                prev.next = start
                start = prev
                prev = n
            return start, k

        while cur:
            count += 1
            temp = cur
            cur = cur.next
            if count == k: 
                # print('----',temp,'*', dummy,'*', cur)
                s, e = reverse(dummy.next, cur)
                # print('++++', s, '*', e)
                if not res:
                    res = s
                else:
                    dummy.next = s    
                e.next = cur
                dummy = e
                count = 0
        return res
                