"""
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:
* If a cell has two adjacent neighbors that are both occupied or both vacant,
then the cell becomes occupied.
* Otherwise, it becomes vacant.

(Note that because the prison is a row, the first and the last cells in the
row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way:
cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days
(and N such changes described above.)

Example 1:
Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation:
    The following table summarizes the state of the prison on each day:
    Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
    Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
    Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
    Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
    Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
    Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
    Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
    Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:
Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]

Note:
cells.length == 8
cells[i] is in {0, 1}
1 <= N <= 10^9

"""

class Solution:
    """
    Runtime: 36 ms, faster than 98.49% of Python3.
    Memory Usage: 13.2 MB, less than 29.68% of Python3.

    Algoritm idea:
        1. The first and last cells become (and left) 0 after the first iteration, so
            we don't count on them.
        2. Having cells.length == 8 and first and last cells out of count, we could have 2**6=64
        possible states for cells. In fact, loop happens earlier and we can spot it,
        this would require from us using some sort of hash map/set to detect if we've seen the result
        of cells modification before. The length of set before the initial state and the state
        with the same value is the length of loop. This is why 14 in 'N = (N - 1) % 14'.
    """
    def prisonAfterNDays(self, cells: list, N: int) -> list:
        while N > 0:
            new_cells = [0] * len(cells)
            for i in range(1, len(cells)-1):
                new_cells[i] = 1 if cells[i-1]==cells[i+1] else 0
            cells = new_cells
            N = (N - 1) % 14
        return cells


if __name__ == "__main__":
    s = Solution()
    assert s.prisonAfterNDays([0,1,0,1,1,0,0,1], 7) == [0,0,1,1,0,0,0,0]
    assert s.prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000) == [0,0,1,1,1,1,1,0]
    assert s.prisonAfterNDays([0,0,0,0,1,1,1,1], 503) == [0,1,0,0,0,0,1,0]
    assert s.prisonAfterNDays([1,0,0,1,0,0,0,1], 826) == [0,1,1,0,1,1,1,0]
