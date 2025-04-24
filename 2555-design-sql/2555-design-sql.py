class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {}
        self.tableRows = {}
        self.numOfCol = {}

        for i in range(len(names)):
            self.tables[names[i]] = {}
            self.tableRows[names[i]] = 1
            self.numOfCol[names[i]] = columns[i]

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.tables or len(row) != self.numOfCol[name]:
            return False
        table = self.tables[name]
        id = self.tableRows[name]
        table[id] = row[:]
        self.tableRows[name] = id + 1
        return True

    def rmv(self, name: str, rowId: int) -> None:
        if name not in self.tables:
            return 
        table = self.tables[name]
        if rowId not in table:
            return 
        del table[rowId]

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.tables or columnId > self.numOfCol[name]:
            return "<null>"
        table = self.tables[name]
        if rowId not in table:
            return "<null>"
        
        return table[rowId][columnId-1]

    def exp(self, name: str) -> List[str]:
        if name not in self.tables:
            return []
        res = []
        table = self.tables[name]
        for id, row in table.items():
            s = str(id) + ',' + ','.join(row)
            res.append(s)
        return res


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)