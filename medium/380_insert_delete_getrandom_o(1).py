"""
Implement the RandomizedSet class:

    bool insert(int val) Inserts an item val into the set if not present.
                         Returns true if the item was not present, false otherwise.
    bool remove(int val) Removes an item val from the set if present.
                         Returns true if the item was present, false otherwise.
    int getRandom()      Returns a random element from the current set of elements (it's guaranteed that at least one
                         element exists when this method is called). Each element must have the same probability of
                         being returned.
Follow up: Could you implement the functions of the class with each function works in average O(1) time?
"""
import random


class RandomizedSet:
    """
    Runtime: 384 ms, faster than 22.28% of Python3
    Memory Usage: 18.5 MB, less than 29.19% of Python3
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set.
        Returns true if the set did not already contain the specified element.
        Time complexity: O(1)
        """
        absent_before = val not in self.data
        self.data.add(val)
        return absent_before

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set.
        Returns true if the set contained the specified element.
        Time complexity: O(1)
        """
        present_before = val in self.data
        if present_before:
            self.data.remove(val)
        return present_before

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        Time complexity: O(n) because of set conversion to tuple
        """
        if self.data:
            return random.choice(tuple(self.data))


if __name__ == '__main__':
    randomizedSet = RandomizedSet()
    assert randomizedSet.insert(1)
    assert randomizedSet.remove(2) is False
    assert randomizedSet.insert(2)
    assert randomizedSet.getRandom() in [1, 2]
    assert randomizedSet.remove(1)
    assert randomizedSet.insert(2)
    assert randomizedSet.getRandom() == 2
