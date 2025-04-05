class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not self.mp[key]:
            return ''
        idx = bisect_right(self.mp[key], [timestamp, '~'])-1
        if idx < 0:
            return ''
        return self.mp[key][idx][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)