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


class RandomizedSet2:
    """
    Runtime: 88 ms, faster than 95.62% of Python3
    Memory Usage: 18.6 MB, less than 11.99% of Python3
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = list()
        self.idxs = dict()  # map value to its index in self.data

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set.
        Returns true if the set did not already contain the specified element.
        Time complexity: O(1)
        """
        absent_before = val not in self.idxs
        if absent_before:
            self.idxs[val] = len(self.data)
            self.data.append(val)
        return absent_before

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set.
        Returns true if the set contained the specified element.
        Time complexity: O(1)
        """
        present_before = val in self.idxs
        if present_before:
            # move the last element to the place idx of the element to delete
            last_element, idx = self.data[-1], self.idxs[val]
            self.data[idx], self.idxs[last_element] = last_element, idx
            # delete the last element
            self.data.pop()
            del self.idxs[val]
        return present_before

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        Time complexity: O(1)
        """
        return random.choice(self.data)


class RandomizedSet3:
    """
    Use dictionary keys as form of set (like it is in Golang)

    Runtime: 360 ms, faster than 26.47% of Python3
    Memory Usage: 18.3 MB, less than 89.84% of Python3
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = dict()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.

        Runtime O(1)
        """
        if val in self.store:
            return False

        self.store[val] = True  # any value is ok, we just need a key
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.

        Runtime O(1)
        """
        if val not in self.store:
            return False

        del self.store[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.

        Runtime: O(N + logN) where O(N) is runtime need to convert keys to tuple and O(log N) is the complexity of
        random.choice(tuple) where n is the number of elements in the tuple. The cpython implementation uses
        _randbelow(len(seq)) to get a pseudo-random index and then returns the item at that index.
        """
        return random.choice(tuple(self.store)) if self.store else None


if __name__ == '__main__':
    solutions = [RandomizedSet(), RandomizedSet2(), RandomizedSet3()]
    for randomizedSet in solutions:
        assert randomizedSet.insert(1)
        assert randomizedSet.remove(2) is False
        assert randomizedSet.insert(2)
        assert randomizedSet.getRandom() in [1, 2]
        assert randomizedSet.remove(1)
        assert randomizedSet.insert(2) is False
        assert randomizedSet.getRandom() == 2
