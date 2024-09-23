class TicTacToe:

    def __init__(self, n: int):
        self.row = [[set(), 0] for _ in range(n)]
        self.col = [[set(), 0] for _ in range(n)]
        self.dia1 = [set(), 0]
        self.dia2 = [set(), 0]
        self.size = n

    def move(self, row: int, col: int, player: int) -> int:
        self.row[row][0].add(player)
        self.row[row][1] += 1
        if self.row[row][1] == self.size and len(self.row[row][0]) == 1:
            return list(self.row[row][0])[0]

        self.col[col][0].add(player)
        self.col[col][1] += 1
        if self.col[col][1] == self.size and len(self.col[col][0]) == 1:
            return list(self.col[col][0])[0]

        if row - col == 0:
            self.dia1[0].add(player)
            self.dia1[1] += 1
            if self.dia1[1] == self.size and len(self.dia1[0]) == 1:
                return list(self.dia1[0])[0]

        if self.size-(row+col+1) == 0:
            self.dia2[0].add(player)
            self.dia2[1] += 1
            if self.dia2[1] == self.size and len(self.dia2[0]) == 1:
                return list(self.dia2[0])[0]
        return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)