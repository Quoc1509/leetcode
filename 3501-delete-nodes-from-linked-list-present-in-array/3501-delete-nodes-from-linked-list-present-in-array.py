# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums =set(nums)
        dummy = ListNode(0, head)
        prev = dummy
        while head:
            if head.val in nums:
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return dummy.next