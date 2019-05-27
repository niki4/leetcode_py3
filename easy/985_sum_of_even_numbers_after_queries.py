"""
We have an array A of integers, and an array queries of queries.

For the i-th query val = queries[i][0], index = queries[i][1],
we add val to A[index].  Then, the answer to the i-th query is
the sum of the even values of A.

(Here, the given index = queries[i][1] is a 0-based index, and
each query permanently modifies the array A.)

Return the answer to all queries.  Your answer array should have
answer[i] as the answer to the i-th query.

Example 1:
Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]

Explanation:
At the beginning, the array is [1,2,3,4].
After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.


Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
1 <= queries.length <= 10000
-10000 <= queries[i][0] <= 10000
0 <= queries[i][1] < A.length
"""

class Solution:
    """
    I personally love this solution, but despite it's correct, the Leetcode
    declines it with Time Limit Exceeded, so it's only for PoC.

    There is optimized algorithm in Solution2 class.
    """
    def sumEvenAfterQueries(self, A: list, queries: list) -> list:
        result = []
        for val, idx in queries:
            A[idx] += val
            result.append(sum(num for num in A if num % 2 == 0))
        return result

class Solution2:
    """
    Runtime: 172 ms, faster than 88.67% of Python3.
    Memory Usage: 17.6 MB, less than 38.51% of Python3.

    The main idea of optimization the abovemontioned algorithm is to precalculate
    the sum of even numbers and use that value at each iteration, adjusting it
    if needed (if old/new value is even).
    """
    def sumEvenAfterQueries(self, A: list, queries: list) -> list:
        result = []
        even_sum = sum(num for num in A if num % 2 == 0)

        for val, idx in queries:
            old_val = A[idx]
            if old_val % 2 == 0:
                even_sum -= old_val

            A[idx] += val
            new_val = A[idx]
            if new_val % 2 == 0:
                even_sum += new_val

            result.append(even_sum)
        return result


if __name__ == "__main__":
    sol = Solution()
    A_1 = [1,2,3,4]
    queries_1 = [[1,0],[-3,1],[-4,0],[2,3]]
    expected_1 = [8,6,2,4]
    assert sol.sumEvenAfterQueries(A_1, queries_1) == expected_1

    sol2 = Solution2()
    A_2 = [1,2,3,4]
    queries_2 = [[1,0],[-3,1],[-4,0],[2,3]]
    expected_2 = [8,6,2,4]
    assert sol2.sumEvenAfterQueries(A_2, queries_2) == expected_2
