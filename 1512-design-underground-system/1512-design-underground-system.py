class UndergroundSystem:

    def __init__(self):
        self.start = {}
        self.mp = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:

        startName, time = self.start[id]
        self.mp[startName, stationName][0] += (t-time)
        self.mp[startName, stationName][1] += 1
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) not in self.mp:
            return 0.0
        return self.mp[(startStation, endStation)][0]/self.mp[(startStation, endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)