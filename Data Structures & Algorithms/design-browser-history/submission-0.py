class BrowserHistory:

    def __init__(self, homepage: str):
        self.sites = [homepage]
        self.i = 0

    def visit(self, url: str) -> None:
        self.sites = self.sites[:self.i + 1]
        self.sites.append(url)
        self.i += 1

    def back(self, steps: int) -> str:
        self.i = max(0, self.i - steps)
        return self.sites[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(len(self.sites) - 1, self.i + steps)
        return self.sites[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)