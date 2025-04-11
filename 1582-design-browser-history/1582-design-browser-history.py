

class BrowserHistory:
    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.cur = 0
        self.length = 1

    def visit(self, url: str) -> None:
        if self.cur == len(self.stack)-1:
            self.stack.append(url)
        else:
            self.stack[self.cur+1] = url
        self.cur += 1
        self.length = self.cur+1

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.stack[self.cur]

    def forward(self, steps: int) -> str:

        self.cur = min(self.cur + steps, self.length-1)
        return self.stack[self.cur]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)