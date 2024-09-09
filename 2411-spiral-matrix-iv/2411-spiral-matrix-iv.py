# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        surround = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = [[-1] * n for _ in range(m)]
        i, row, col = 0, 0, 0
        while head:
            res[row][col] = head.val
            head = head.next
            next_row, next_col = row+surround[i][0], col+surround[i][1]
            if 0 <= next_row < m and 0 <= next_col < n and res[next_row][next_col] == -1:
                row, col = next_row, next_col  # Move to the next position
            else:
                # Change direction if the next position is out of bounds or already visited
                i = (i+ 1) % 4  # Update direction (right → down → left → up)
                row += surround[i][0]
                col += surround[i][1]
        return res