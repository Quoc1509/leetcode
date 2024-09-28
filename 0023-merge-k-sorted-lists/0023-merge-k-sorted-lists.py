# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # heap = []
        # for i in lists:
        #     cur = i
        #     while cur:
        #         heappush(heap, (cur.val))
        #         cur = cur.next
        # head = None
        # cur = head
        # while heap:
        #     b = heappop(heap)
        #     if not head:     
        #         head = ListNode(b, None)
        #         cur = head
        #     else:
        #         cur.next = ListNode(b, None)
        #         cur = cur.next
        # return head

        def conquer(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            cur1 = l1
            cur2 = l2
            begin = None
            cur = begin
            while cur1 and cur2:
                if cur1.val < cur2.val:
                    if not begin:
                        begin = cur1
                        cur = begin             
                    else:
                        cur.next = cur1
                        cur = cur.next
                    cur1 = cur1.next
                else:
                    if not begin:
                        begin = cur2
                        cur = begin
                        
                    else:
                        cur.next = cur2
                        cur = cur.next
                    cur2 = cur2.next

            if cur1:
                cur.next = cur1
            if cur2:
                cur.next = cur2
            
            return begin


        def devide(link):
            if not link: return None
            if len(link) == 1:
                return link[0]
            half = len(link)//2
            l1 = devide(link[:half])
            l2 = devide(link[half:])
            return conquer(l1, l2)
        
        head = devide(lists)
        return head

            
