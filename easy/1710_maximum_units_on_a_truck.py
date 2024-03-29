"""
You are assigned to put some amount of boxes onto one truck.
You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck.
You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

Example 1:
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

Example 2:
Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91

Constraints:
    1 <= boxTypes.length <= 1000
    1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
    1 <= truckSize <= 106
"""
from typing import List

class Solution:
    """
    Time complexity: O(n logN)
    Space complexity: O(n)
    """
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        most_to_less_exp_boxes = sorted(boxTypes, key=lambda box_type: box_type[1], reverse=True)
        max_units_to_put = 0

        for box_type in most_to_less_exp_boxes:
            curr_type_box_amount, units_per_box = box_type
            while curr_type_box_amount > 0 and truckSize > 0:
                max_units_to_put += units_per_box
                curr_type_box_amount -= 1
                truckSize -= 1

        return max_units_to_put


if __name__ == '__main__':
    sol = Solution()
    test_cases = (
        ([[1,3],[2,2],[3,1]], 4, 8),
        ([[5,10],[2,5],[4,7],[3,9]], 10, 91),
    )
    for box_types, truck_size, exp_res in test_cases:
        assert sol.maximumUnits(box_types, truck_size) == exp_res
