"""
Suppose Andy and Doris want to choose a restaurant for dinner,
and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum.
If there is a choice tie between answers, output all of them with no order requirement.
You could assume there always exists an answer.

Example 1:
Input:
list1 = ["Shogun","Tapioca Express","Burger King","KFC"],
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
"""
from typing import List


class Solution:
    """
    Bruteforce approach.
    Traverse either list; if restaurant also present in another list - find indexes and calc sum of both restaurants;
    Collect sum of indexes in a hash map, then sort it by value; Return all names for those rest where is min idx sum.

    Runtime: 324 ms, faster than 12.84% of Python3
    Memory Usage: 14.8 MB, less than 42.90% of Python3
    """

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        idx_sums = dict()
        for rest in list1:
            if rest in list2:
                idx_sums[rest] = list1.index(rest) + list2.index(rest)
        min_rest = min(idx_sums, key=idx_sums.get)
        min_idx_sum = idx_sums[min_rest]
        return [k for (k, v) in idx_sums.items() if v == min_idx_sum]


class Solution2:
    """
    Optimized first solution

    Runtime: 312 ms, faster than 13.75% of Python3
    Memory Usage: 14.9 MB, less than 15.18% of Python3
    """

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        idx_sums = dict()
        common = set(list1).intersection(list2)
        min_idx_sum = float('+inf')
        for rest in common:
            idx_sums[rest] = list1.index(rest) + list2.index(rest)
            min_idx_sum = min(min_idx_sum, idx_sums[rest])

        return [k for k in idx_sums if idx_sums[k] == min_idx_sum]


class Solution3:
    """
    Another optimization - reducing number of .index() calls to single pass over each list.

    Runtime: 168 ms, faster than 44.64% of Python3
    Memory Usage: 14.9 MB, less than 15.18% of Python3
    """

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        idx_sums = dict()
        min_idx_sum = float('+inf')
        list1_idx = {v: i for (i, v) in enumerate(list1)}
        for i, rest in enumerate(list2):
            if rest in list1_idx:
                idx_sums[rest] = i + list1_idx[rest]
                min_idx_sum = min(min_idx_sum, idx_sums[rest])
        return [r for r in idx_sums if idx_sums[r] == min_idx_sum]


class Solution4:
    """
    Further optimization - keep the list of restaurants with smallest index sum only

    Runtime: 164 ms, faster than 46.30% of Python3
    Memory Usage: 14.9 MB, less than 15.18% of Python3

    Time complexity: O(l1+l2). Every item of list2 is checked in a map of list1.
    l1 and l2 are the lengths of list1 and list2 respectively.
    Space complexity: O(l1∗x). hashmap size grows upto l1∗x, where x refers to average string length.
    """

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = list()
        min_idx_sum = float('+inf')
        list1_idx = {v: i for (i, v) in enumerate(list1)}

        for i, rest in enumerate(list2):
            if rest in list1_idx:
                idx_sum = i + list1_idx[rest]
                if idx_sum < min_idx_sum:
                    result = [rest]
                    min_idx_sum = idx_sum
                elif idx_sum == min_idx_sum:
                    result.append(rest)
        return result


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3(), Solution4()]
    tc = (
        (["Shogun", "Tapioca Express", "Burger King", "KFC"],
         ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"],
         ["Shogun"]),
        (["Shogun", "Tapioca Express", "Burger King", "KFC"],
         ["KFC", "Shogun", "Burger King"],
         ["Shogun"]),
        (["Shogun", "Tapioca Express", "Burger King", "KFC"],
         ["KFC", "Burger King", "Tapioca Express", "Shogun"],
         ["KFC", "Burger King", "Tapioca Express", "Shogun"]),
        (["Shogun", "Tapioca Express", "Burger King", "KFC"],
         ["KNN", "KFC", "Burger King", "Tapioca Express", "Shogun"],
         ["KFC", "Burger King", "Tapioca Express", "Shogun"]),
        (["KFC"], ["KFC"], ["KFC"]),
        (["Shogun", "Tapioca Express", "Burger King", "KFC"],
         ["KFC", "Shogun", "Burger King"],
         ["Shogun"]),
    )
    for s in solutions:
        for inp_l1, inp_l2, exp in tc:
            res = s.findRestaurant(inp_l1, inp_l2)
            assert sorted(res) == sorted(exp), f"expected {sorted(exp)}, got {sorted(res)}"
