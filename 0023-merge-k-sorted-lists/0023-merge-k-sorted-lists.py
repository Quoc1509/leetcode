# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # mp = defaultdict(list)
        for i, node in enumerate(lists):
            if not node:
                continue
            heappush(heap, (node.val, i, node))
            # mp[node.val].append(node)
        dummy = pre = ListNode(0, None)
        while heap:
            val, i, node = heappop(heap)
            
            pre.next = node
            pre = pre.next
            if node.next:
                heappush(heap, (node.next.val, i, node.next))
        return dummy.next


            
