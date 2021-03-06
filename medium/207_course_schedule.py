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


class Solution2:
    """
    Post-Order DFS + Backtracking.

    Algorithm: "with the above backtracking algorithm, we would visit certain nodes multiple times, which is not the
    most efficient way. To optimize it, once we've done the check that there would be no cycle formed starting from this
    node, we don't have to do the same check for all the nodes in the downstream.

    We could implement the Post-order DFS (depth-first search, in post-order strategy we visit a node's descendant nodes
    before the node itself) based on the above backtracking algorithm, by simply adding another bitmap (i.e.
    checked[node_index]) which indicates whether we have done the cyclic check starting from a particular node.

    Here are breakdowns of the algorithm, where the first 2 steps are the same as in previous backtracking algorithm.

    1. We build a graph data structure from the given list of course dependencies.
    2. We then enumerate each node (course) in the constructed graph, to check if we could form a dependency cycle
       starting from the node.
    3.1 We check if the current node has been checked before, otherwise we enumerate through its child nodes via
       backtracking, where we breadcrumb our path (i.e. mark the nodes we visited) to detect if we come across a
       previously visited node (hence a cycle detected). We also remove the breadcrumbs for each iteration.
    3.2 Once we visited all the child nodes (i.e. postorder), we mark the current node as checked."

    Runtime: 96 ms, faster than 73.74% of Python3
    Memory Usage: 16.5 MB, less than 50.78% of Python3

    Time/Space Complexity: O(∣E∣+∣V∣) where |V| is the number of courses, and |E| is the number of dependencies.
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dict = collections.defaultdict(list)

        for relation in prerequisites:
            next_course, prev_course = relation
            course_dict[prev_course].append(next_course)

        checked = [False] * numCourses
        path = [False] * numCourses

        for curr_course in range(numCourses):
            if self.is_cyclic(curr_course, course_dict, checked, path):
                return False
        return True

    def is_cyclic(self, curr_course, course_dict, checked, path):
        """
        Backtracking method to check that no cycle would be formed starting from curr_course
        """
        # 1. Bottom-cases
        if checked[curr_course]:  # the node has been checked, no cycle would be formed from it.
            return False
        if path[curr_course]:  # come across a previously visited node, thus cycle detected
            return True

        # 2. Post-order DFS (so children visited before its parent)
        path[curr_course] = True  # before backtracking, mark the node in the path

        is_cycle_found = False
        for child in course_dict[curr_course]:
            is_cycle_found = self.is_cyclic(child, course_dict, checked, path)
            if is_cycle_found:
                break

        # 3. after the visits of children, we come back to process the node itself
        path[curr_course] = False  # backtrack (remove the node from the path)

        # Now that we've visited the nodes in the downstream, we complete the check of this node.
        checked[curr_course] = True
        return is_cycle_found


class GNode:
    """ data structure represent a vertex in the graph """

    def __init__(self):
        self.inDegrees = 0  # num of dependent nodes (prerequisites)
        self.outNodes = []


class Solution3:
    """
    Topological Sort

    "The algorithm is about find a global order for all nodes in a DAG (Directed Acyclic Graph) with regarding to their
    dependencies. To better understand the algorithm, we summarize a few points here:
        * In order to find a global order, we can start from those nodes which do not have any prerequisites (i.e.
            indegree of node is zero), we then incrementally add new nodes to the global order, following the
            dependencies (edges).
        * Once we follow an edge, we then remove it from the graph.
        * With the removal of edges, there would more nodes appearing without any prerequisite dependency, in addition
            to the initial list in the first step.
        * The algorithm would terminate when we can no longer remove edges from the graph.
          There are two possible outcomes:
            1. If there are still some edges left in the graph, then these edges must have formed certain cycles,
                which is similar to the deadlock situation. It is due to these cyclic dependencies that we cannot remove
                them during the above processes.
            2. Otherwise, i.e. we have removed all the edges from the graph, and we got ourselves a topological order
                of the graph."

    Runtime: 92 ms, faster than 89.55% of Python3
    Memory Usage: 15.2 MB, less than 99.85% of Python3

    Time/Space Complexity: O(∣E∣+∣V∣) where |V| is the number of courses, and |E| is the number of dependencies.
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(GNode)  # key: index of node; value: GNode

        total_deps = 0
        for relation in prerequisites:
            next_course, prev_course = relation
            graph[prev_course].outNodes.append(next_course)
            graph[next_course].inDegrees += 1
            total_deps += 1

        # we start from courses that have no prerequisites;
        # we could use either set, stack of queue to keep track of courses with no dependence.
        no_dep_courses = collections.deque()  # regular stack, e.g. list(), works here too
        for index, node in graph.items():
            if node.inDegrees == 0:
                no_dep_courses.append(index)

        removed_edges = 0
        while no_dep_courses:
            course = no_dep_courses.pop()

            # remove course's outgoing edges one by one
            for next_course in graph[course].outNodes:
                graph[next_course].inDegrees -= 1
                removed_edges += 1
                # while removing edges, we might discover new courses with prerequisites removed,
                # i.e. new courses without prerequisites.
                if graph[next_course].inDegrees == 0:
                    no_dep_courses.append(next_course)

        if removed_edges == total_deps:  # it's a DAG, so we can reach end from start
            return True
        else:  # dead-lock (dependencies), we cannot remove the cyclic edges
            return False


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (3, [[1, 0], [2, 0]], True),  # before we can take course 1 or 2 we need to take course 0 first
    )
    for sol in solutions:
        for in_numCourses, in_prerequisites, exp_can_finish in tc:
            result = sol.canFinish(in_numCourses, in_prerequisites)
            assert result is exp_can_finish, f"{sol.__class__.__name__}: expected {exp_can_finish}, got {result}"
