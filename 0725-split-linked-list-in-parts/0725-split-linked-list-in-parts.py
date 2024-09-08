# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        l = [length//k] * k
        res = []
        extra = length % k
        for i in range(extra):
            l[i] += 1
        count = 0
        cur = head
        while cur:
            res.append(cur)
            temp = cur
            for i in range(l[count]):
                if i == l[count]-1:
                    cur = temp.next
                    temp.next = None
                    break
                temp = temp.next
            count += 1
        res.extend([None] * (k-len(res)))
        return res 
        