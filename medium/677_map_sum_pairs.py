"""
Implement the MapSum class:
        MapSum() Initializes the MapSum object.
        void insert(String key, int val) Inserts the key-val pair into the map.
            If the key already existed, the original key-value pair will be overridden to the new one.
        int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.

Example 1:
    Input
    ["MapSum", "insert", "sum", "insert", "sum"]
    [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
    Output
    [null, null, 3, null, 5]

Explanation
    MapSum mapSum = new MapSum();
    mapSum.insert("apple", 3);
    mapSum.sum("ap");           // return 3 (apple = 3)
    mapSum.insert("app", 2);
    mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)

Constraints:
    1 <= key.length, prefix.length <= 50
    key and prefix consist of only lowercase English letters.
    1 <= val <= 1000
    At most 50 calls will be made to insert and sum.
"""


class MapSum:
    """
    Runtime: 44 ms, faster than 5.91% of Python3
    Memory Usage: 14.3 MB, less than 79.73% of Python3
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = dict()

    def insert(self, key: str, val: int) -> None:
        self.hash_map[key] = val

    def sum(self, prefix: str) -> int:
        return sum(val for (key, val) in self.hash_map.items() if key.startswith(prefix))


if __name__ == '__main__':
    solutions = [MapSum()]
    for map_sum in solutions:
        map_sum.insert("apple", 3)
        assert map_sum.sum("ap") == 3  # (apple=3)
        map_sum.insert("app", 2)
        assert map_sum.sum("ap") == 5  # (apple + app = 3 + 2 = 5)
