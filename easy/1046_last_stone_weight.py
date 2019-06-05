"""

"""

class Solution:
    """
    Runtime: 28 ms, faster than 97.02% of Python3.
    Memory Usage: 13.2 MB, less than 100.00% of Python3.
    """
    def lastStoneWeight(self, stones: list) -> int:
        while len(stones) > 1:
            y = max(stones)
            y_idx = stones.index(y)
            temp_stones = stones[:y_idx] + [0] + stones[y_idx+1:]  # skip 'y' value from search and keep indexing order
            x = max(temp_stones)
            x_idx = temp_stones.index(x)

            if x == y:
                del stones[x_idx]
                del stones[y_idx]
            else:
                stones[y_idx] = y - x
                del stones[x_idx]

        return stones.pop() if stones else 0


if __name__ == "__main__":
    s = Solution()
    assert s.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert s.lastStoneWeight([10, 4, 2, 10]) == 2
