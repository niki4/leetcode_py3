"""
Design a logger system that receives a stream of messages along with their timestamps.
Each unique message should only  be printed at most every 10 seconds (i.e. a message printed at timestamp t will
prevent other identical messages from being printed until timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the Logger class:
    Logger() Initializes the logger object.
    bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given
timestamp, otherwise returns false.

"""


class Logger:
    """
    Runtime: 144 ms, faster than 65.48% of Python3
    Memory Usage: 20.1 MB, less than 75.42% of Python3

    Time Complexity: O(1). The lookup and update of the hashtable takes a constant time.
    Space Complexity: O(M) where M is the size of all incoming messages.
    Over the time, the hashtable would have an entry for each unique message that has appeared.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.records = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.records:
            self.records[message] = timestamp
            return True

        old_ts = self.records[message]
        if timestamp >= old_ts + 10:
            self.records[message] = timestamp
            return True

        return False


if __name__ == '__main__':
    logger = Logger()
    assert logger.shouldPrintMessage(1, "foo") is True  # next allowed timestamp for "foo" is 1 + 10 = 11
    assert logger.shouldPrintMessage(2, "bar") is True  # next allowed timestamp for "bar" is 2 + 10 = 12
    assert logger.shouldPrintMessage(3, "foo") is False  # 3 < 11
    assert logger.shouldPrintMessage(8, "bar") is False  # 8 < 12
    assert logger.shouldPrintMessage(10, "foo") is False  # 10 < 11
    assert logger.shouldPrintMessage(11, "foo") is True  # 11 >= 11, next allowed timestamp for "foo" is 11 + 10 = 21

    assert logger.shouldPrintMessage(100, "bug") is True
    assert logger.shouldPrintMessage(100, "bug") is False  # two equal messages at the same ts is not allowed
