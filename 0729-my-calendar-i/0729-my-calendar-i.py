class MyCalendar:

    def __init__(self):
        self.schedule = []

    def book(self, start: int, end: int) -> bool:
        if len(self.schedule) == 0:
            self.schedule.append([start, end])
            return True
        if start >= self.schedule[-1][1] or end <= self.schedule[0][0]:
            self.schedule.append([start, end])
            self.schedule.sort()
            return True
        l, r = 0, len(self.schedule)-1
        m = 0
        while l <= r:
            m = (l+r)//2
            if start >= self.schedule[m][1] and end <= self.schedule[m+1][0]:
                self.schedule.append([start, end])
                self.schedule.sort()
                return True
            elif start >= self.schedule[m][1]:
                l = m + 1
            else:
                r = m - 1
        return False
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)