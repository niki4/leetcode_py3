"""
You are given a data structure of employee information,
which includes the employee's unique id, his importance
value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2,
and employee 2 is the leader of employee 3.
They have importance value 15, 10 and 5, respectively.
Then employee 1 has a data structure like [1, 15, [2]],
and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []].
Note that although employee 3 is also a subordinate of employee 1,
the relationship is not direct.

Now given the employee information of a company, and an employee id,
you need to return the total importance value of this employee and
all his subordinates.

Example 1:
    Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
    Output: 11

Explanation:
Employee 1 has importance value 5, and he has two direct
subordinates: employee 2 and employee 3. They both have importance value 3.
So the total importance value of employee 1 is 5 + 3 + 3 = 11.

Note:

One employee has at most one direct leader and may have several subordinates.
The maximum number of employees won't exceed 2000.
"""

# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution:
    """
    Runtime: 260 ms, faster than 7.90% of Python3.
    Memory Usage: 14.2 MB, less than 69.47% of Python3.

    Iterating over list in order to find next employee is slow.
    """

    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        if not employees:
            return 0

        total_importance = 0
        leader_subords = []
        visited = []

        for employee in employees:
            if employee.id == id:
                leader_subords = employee.subordinates
                total_importance += employee.importance

        while leader_subords:
            subord_id = leader_subords.pop()
            if subord_id in visited:
                continue

            for employee in employees:
                if employee.id == subord_id:
                    total_importance += employee.importance
                    visited.append(subord_id)
                    if employee.subordinates:
                        leader_subords = employee.subordinates + leader_subords
        return total_importance


class Solution2:
    """
    Runtime: 196 ms, faster than 83.04% of Python3.
    Memory Usage: 14.1 MB, less than 91.28% of Python3.

    Depth-First Search recursive approach + hashmap for O(1) lookup
    """
    def getImportance(self, employees, query_id):
        empl_map = {empl.id: empl for empl in employees}
        def dfs(empl_id):
            employee = empl_map[empl_id]
            return (employee.importance + sum(
                dfs(subord_empl_id) for subord_empl_id in employee.subordinates))
        return dfs(query_id)


if __name__ == "__main__":
    s = Solution()
    s2 = Solution2()

    test_employees_1 = [
        Employee(1, 5, [2, 3]),
        Employee(2, 3, []),
        Employee(3, 3, []),
        ]
    test_employees_2 = [
        Employee(1, 2, [2]),
        Employee(2, 3, []),
        ]

    test_leader_id_1 = 1
    test_leader_id_2 = 2

    expected_result_1 = 11
    expected_result_2 = 3

    assert s.getImportance(test_employees_1, test_leader_id_1) == expected_result_1
    assert s2.getImportance(test_employees_2, test_leader_id_2) == expected_result_2
