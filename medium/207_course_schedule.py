"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [Ai, Bi] indicates that you must take course Bi first
if you want to take course Ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take.
    To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take.
    To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1.
    So it is impossible.

Constraints:
    1 <= numCourses <= 105
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= Ai, Bi < numCourses
    All the pairs prerequisites[i] are unique.
"""
import collections
from typing import List


class Solution:
    """
    Backtracking.

    Algorithm: "the problem to determine if one could build a valid schedule of courses that satisfies all the
    dependencies (i.e. constraints) would be equivalent to determine if the corresponding graph is a DAG (
    Directed Acyclic Graph), i.e. there is no cycle existed in the graph.

    Backtracking is a general algorithm that is often applied to solve the constraint satisfaction problems, which
    incrementally builds candidates to the solutions, and abandons a candidate (i.e. backtracks) as soon as it
    determines that the candidate would not lead to a valid solution.

    1. First build a graph data structure from the given list of course dependencies. Here we adopt the adjacency list
    as shown (https://leetcode.com/problems/course-schedule/Figures/207/207_adjacency_list.png) to represent the graph,
    which can be implemented via hashmap or dictionary. Each entry in the adjacency list represents a node which
    consists of a node index and a list of neighbors nodes that follow from the node.
    2. Then enumerate each node (course) in the constructed graph, to check if we could form a dependency cycle
    starting from the node.
    3. Perform the cyclic check via backtracking, where we breadcrumb our path (i.e. mark the nodes we visited) to
    detect if we come across a previously visited node (hence a cycle detected). We also remove the breadcrumbs for
    each iteration.
    "

    Got TLE (timeout) from LC.

    Time Complexity: O(∣E∣ + ∣V∣^2) where |E| is the number of dependencies, |V| is the number of courses and d is the
    maximum length of acyclic paths in the graph.
    Space complexity: Time Complexity: O(∣E∣ + ∣V∣)
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dict = collections.defaultdict(list)

        for relation in prerequisites:
            next_course, prev_course = relation
            course_dict[prev_course].append(next_course)

        path = [False] * numCourses
        for curr_course in range(numCourses):
            if self.is_cyclic(curr_course, course_dict, path):
                return False
        return True

    def is_cyclic(self, curr_course, course_dict, path):
        """
        Backtracking method to check that no cycle would be formed starting from curr_course
        """
        if path[curr_course]:  # come across a previously visited node, thus cycle detected
            return True

        path[curr_course] = True  # before backtracking, mark the node in the path

        is_cycle_found = False
        for child in course_dict[curr_course]:
            is_cycle_found = self.is_cyclic(child, course_dict, path)
            if is_cycle_found:
                break

        path[curr_course] = False  # backtrack (remove the node from the path)
        return is_cycle_found


if __name__ == '__main__':
    solutions = [Solution()]
    tc = (
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (3, [[1, 0], [2, 0]], True),  # before we can take course 1 or 2 we need to take course 0 first
    )
    for sol in solutions:
        for in_numCourses, in_prerequisites, exp_can_finish in tc:
            result = sol.canFinish(in_numCourses, in_prerequisites)
            assert result is exp_can_finish, f"{sol.__class__.__name__}: expected {exp_can_finish}, got {result}"
