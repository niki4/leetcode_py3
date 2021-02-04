"""
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);
hashMap.put(2, 2);
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found)

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
"""


class MyHashMap:
    """
    Approach: Modulo + Array

    Runtime: 204 ms, faster than 85.47% of Python3
    Memory Usage: 17.4 MB, less than 70.92% of Python3
    You may play with the pre-allocated (number of buckets) space for the storage to find best score for your input.

    Time Complexity: for each of the methods, the time complexity is O(N/K) where N is the number of all possible keys
    and K is the number of predefined buckets in the hashmap, which is 769 in our case.
    Space Complexity: O(K+M) where K is the number of predefined buckets in the hashmap and M is the number of unique
    keys that have been inserted into the hashmap.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = [list() for _ in range(769)]  # pre-allocate space for 769 keys/buckets

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % len(self.store)
        for i, item in enumerate(self.store[idx]):
            if item[0] == key:
                self.store[idx][i] = (key, value)
                return
        # case if no specified key in bucket - create one
        self.store[idx].append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % len(self.store)
        for k, v in self.store[idx]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % len(self.store)
        self.store[idx] = [item for item in self.store[idx] if item[0] != key]


if __name__ == '__main__':
    hashMap = MyHashMap()
    hashMap.put(1, 1)
    hashMap.put(2, 2)
    assert hashMap.get(1) == 1
    assert hashMap.get(3) == -1  # (not found)
    hashMap.put(2, 1)  # update the existing value
    assert hashMap.get(2) == 1
    hashMap.remove(2)  # remove the mapping for 2
    assert hashMap.get(2) == -1  # returns -1 (not found)
