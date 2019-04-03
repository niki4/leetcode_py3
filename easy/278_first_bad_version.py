"""
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version,
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first
 bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether
version is bad. Implement a function to find the first bad version.
You should minimize the number of calls to the API.

Example:
Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
"""


class Solution:
    """
    Naive linear approach. Good only to small ranges.
    As expected, got 'Time Limit Exceeded'
    """
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = n - 1
        while isBadVersion(first) and first > 0:
            first -= 1

        return first + 1

    """
    Binary search. Reducing the whole searching set twice at each iteration.
    
    Runtime: 36 ms, faster than 66.54% of Python3.
    Memory Usage: 13 MB, less than 6.19% of Python3.
    Runtime complexity: O(log n)
    """
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        last = n

        while first < last:
            mid = (first + last) // 2
            if isBadVersion(mid):
                last = mid
            else:
                first = mid + 1
        return first
