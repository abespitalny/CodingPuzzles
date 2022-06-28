'''
You have a browser of one tab where you start on the homepage and you can visit another url,
get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:
    - BrowserHistory(string homepage)
        Initializes the object with the homepage of the browser.
    - void visit(string url)
        Visits url from the current page. It clears up all the forward history.
    - string back(int steps)
        Move steps back in history.
        If you can only return x steps in the history and steps > x, you will return only x steps.
        Return the current url after moving back in history at most steps.
    - string forward(int steps)
        Move steps forward in history.
        If you can only forward x steps in the history and steps > x, you will forward only x steps.
        Return the current url after forwarding in history at most steps.
'''

# Time: O(1) for all operations.
# Space: O(n) for storing the URLs.
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.numUrls = 1
        self.pageIdx = 0

    def visit(self, url: str) -> None:
        self.pageIdx += 1
        if self.pageIdx == len(self.history):
            self.history.append(url)
            self.numUrls += 1
        else:
            self.history[self.pageIdx] = url
            self.numUrls = self.pageIdx + 1

    def back(self, steps: int) -> str:
        self.pageIdx = max(0, self.pageIdx - steps)
        return self.history[self.pageIdx]

    def forward(self, steps: int) -> str:
        self.pageIdx = min(self.numUrls - 1, self.pageIdx + steps)
        return self.history[self.pageIdx]


browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
assert browserHistory.back(1) == "facebook.com"
assert browserHistory.back(1) == "google.com"
assert browserHistory.forward(1) == "facebook.com"
browserHistory.visit("linkedin.com")
assert browserHistory.forward(2) == "linkedin.com"
assert browserHistory.back(2) == "google.com"
assert browserHistory.back(7) == "leetcode.com"
