# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in lists:
            cur = i
            while cur:
                heappush(heap, (cur.val))
                cur = cur.next
        head = None
        cur = head
        while heap:
            b = heappop(heap)
            if not head:     
                head = ListNode(b, None)
                cur = head
            else:
                cur.next = ListNode(b, None)
                cur = cur.next
        return head
            
