class LogSystem:

    def __init__(self):
        
        self.logList = SortedList()

        self.temp = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19

        }

    def put(self, id: int, timestamp: str) -> None:
        time = []
        self.logList.add((timestamp, id))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        res = []
        start = start[:self.temp[granularity]]
        end = end[:self.temp[granularity]]

        idx = self.logList.bisect_left((start, -1))

        while idx < len(self.logList) and self.logList[idx][0][:self.temp[granularity]] <= end:
            res.append(self.logList[idx][1])
            idx += 1 
        return res