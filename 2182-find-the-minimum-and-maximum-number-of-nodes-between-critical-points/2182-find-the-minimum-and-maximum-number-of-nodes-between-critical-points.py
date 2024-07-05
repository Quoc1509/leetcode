# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = [inf, -inf]
        first, second = None, None
        count = 2
        pre = head
        head = head.next
        while head.next:
            if (head.val > pre.val and head.val > head.next.val) or (head.val < pre.val and head.val < head.next.val):
                if first is None : second = first = count
                else:
                    res[0] = min(res[0], count - second)
                    res[1] = max(res[1], count - first)
                    # print(count, first, second)
                    second = count
                # print(count, first, second)
            pre = head
            count += 1
            head = head.next

        return res if res[0] != inf and res[1] != -inf else [-1, -1]