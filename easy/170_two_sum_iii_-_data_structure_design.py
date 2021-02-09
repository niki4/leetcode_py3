"""
Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to
a particular value.

Implement the TwoSum class:
    TwoSum()                Initializes the TwoSum object, with an empty array initially.
    void add(int number)    Adds number to the data structure.
    boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value,
                            otherwise, it returns false.
"""


class TwoSum:
    """
    Runtime: 388 ms, faster than 53.43% of Python3
    Memory Usage: 20.3 MB, less than 86.80% of Python3
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = list()

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums.append(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        seen = set()
        for n in self.nums:
            if value - n in seen:
                return True
            seen.add(n)
        return False


if __name__ == '__main__':
    twoSum = TwoSum()
    twoSum.add(1)
    twoSum.add(3)
    twoSum.add(5)
    assert twoSum.nums == [1, 3, 5]
    assert twoSum.find(4) is True  # 1 + 3 = 4
    assert twoSum.find(7) is False
