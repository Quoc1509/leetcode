class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        s = sum(milestones)
        m = max(milestones)
        if s - m < m:
            return (s-m)*2 + 1
        return s