# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        nums = set(nums)
        cur = dummy = ListNode(0, head)
        while head:
            while head and head.val in nums:
                head = head.next
            dummy.next = head
            dummy = dummy.next
            if head:
                head = head.next
        return cur.next