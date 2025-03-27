# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        mp = defaultdict(list)
        for node in lists:
            if not node:
                continue
            heappush(heap, node.val)
            mp[node.val].append(node)
        dummy = pre = ListNode(0, None)
        while heap:
            v = heappop(heap)
            n = mp[v].pop()
            pre.next = n
            pre = pre.next
            if n.next:
                heappush(heap, (n.next.val))
                mp[n.next.val].append(n.next)
        return dummy.next


            
