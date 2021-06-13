"""
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history
number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:
-    BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
-    void visit(string url) Visits url from the current page. It clears up all the forward history.
-    string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x,
        you will return only x steps. Return the current url after moving back in history at most steps.
-    string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and
        steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

Constraints:
    1 <= homepage.length <= 20
    1 <= url.length <= 20
    1 <= steps <= 100
    homepage and url consist of  '.' or lower case English letters.
    At most 5000 calls will be made to visit, back, and forward.
"""


class DoubleLinkedList:
    def __init__(self, val=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = None


class BrowserHistory:
    """
    Double Linked List works perfectly if we need to move back and forward with the history.
    We only need to keep track the current position (node) in our history.

    Runtime: 308 ms, faster than 36.71% of Python3
    Memory Usage: 16.7 MB, less than 34.01% of Python3

    Time complexity: O(1) for visit. O(n) for back and forward, where n is the number of nodes in the list.
    Space complexity: O(n)
    """

    def __init__(self, homepage: str):
        self.curr = DoubleLinkedList(homepage)

    def visit(self, url: str) -> None:
        self.curr.next = DoubleLinkedList(val=url, prev=self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while steps:
            if not self.curr.prev:
                break
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while steps:
            if not self.curr.next:
                break
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val


if __name__ == '__main__':
    bh = BrowserHistory("leetcode.com")
    # You are in "leetcode.com". Visit "google.com"
    bh.visit("google.com")
    # You are in "google.com". Visit "facebook.com"
    bh.visit("facebook.com")
    # You are in "facebook.com". Visit "youtube.com"
    bh.visit("youtube.com")
    # You are in "youtube.com", move back to "facebook.com"
    assert bh.back(1) == "facebook.com"
    # You are in "facebook.com", move back to "google.com"
    assert bh.back(1) == "google.com"
    # You are in "google.com", move forward to "facebook.com"
    assert bh.forward(1) == "facebook.com"
    # You are in "facebook.com". Visit "linkedin.com"
    bh.visit("linkedin.com")
    # You are in "linkedin.com", you cannot move forward any steps.
    bh.forward(2)
    # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com"
    assert bh.back(2) == "google.com"
    # You are in "google.com", you can move back only one step to "leetcode.com"
    assert bh.back(7) == "leetcode.com"
