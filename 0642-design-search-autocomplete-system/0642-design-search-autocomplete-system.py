class Node:
    def __init__(self, parent=None):
        self.next = {}
        self.parent = parent
        self.top3 = []
        self.end = -1

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.sentences = sentences[:]
        self.times = times[:]
        self.count = len(times)
        self.root = Node()
        self.curStr = ""
        self.cur = self.root
        for i, s in enumerate(sentences):
            cur = self.root
            for c in s:
                if c not in cur.next:
                    cur.next[c] = Node(cur)
                cur = cur.next[c]
                self.update(cur, i)
            cur.end = i

    def update(self, cur, i):
        if i in cur.top3:
            return
        if len(cur.top3) < 3:
            cur.top3.append(i)
        else:
            minView = inf
            idx = 0
            for j in range(3):
                if self.times[cur.top3[j]] < minView:
                    minView = self.times[cur.top3[j]]
                    idx = j
                elif self.times[cur.top3[j]] == minView and self.sentences[cur.top3[j]] > self.sentences[cur.top3[idx]]:
                    idx = j


            if self.times[i] > self.times[cur.top3[idx]] or (self.times[i] == self.times[cur.top3[idx]] and self.sentences[i] < self.sentences[cur.top3[idx]]):
                cur.top3[idx] = i
            

    def input(self, c: str) -> List[str]:
        if c == "#":
            if self.cur.end == -1:
                self.cur.end = self.count
                self.times.append(1)
                self.sentences.append(self.curStr)
                self.count += 1
            else:
                self.times[self.cur.end] += 1
            i = self.cur.end
            while self.cur != self.root:
                self.update(self.cur, i)
                self.cur = self.cur.parent
            self.curStr = ""

            return []
        else:
            self.curStr += c
            if c not in self.cur.next:
                self.cur.next[c] = Node(self.cur)
            self.cur = self.cur.next[c]
            res = [self.sentences[i] for i in sorted(self.cur.top3, key=lambda i: [-self.times[i], self.sentences[i]])]
            return res


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)