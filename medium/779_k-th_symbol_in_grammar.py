"""
On the first row, we write a 0. 
Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
"""

class Solution(object):
    """
    Bruteforce solution. TLE (doesn't work for quite large N as we double row at each iteration).
    """
    def kthGrammar(self, N, K):
        lastrow = '0'
        while len(lastrow) < 2**N:
            lastrow = "".join('01' if x == '0' else '10' for x in lastrow)
        return int(lastrow[K-1])


class Solution2:
    """
    Recursive approach.
    In general, the Kth digit's parent is going to be (K+1) // 2. 
    If the parent is 0, then the digit will be the same as 1 - (K%2). 
    If the parent is 1, the digit will be the opposite, ie. K%2.
    
    Runtime: 32 ms, faster than 41.79% of Python3
    Memory Usage: 14.2 MB, less than 100.00% of Python3
    Time Complexity: O(N)
    Space Complexity: O(N) (to hold stack of recursive calls)
    """
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        return (1 - K%2) ^ self.kthGrammar(N-1, (K+1)//2)


class Solution3:
    """
    As in Approach #2, we could try to write the bit in terms of it's previous bit.
    When writing a few rows of the sequence, we notice a pattern: 
    the second half is always the first half "flipped": namely, that '0' becomes '1' and '1' becomes '0'. 
    
    We can prove this assertion by induction. The key idea is if a string X generates Y, then a flipped string X' generates Y'.

    This leads to the following algorithm idea: if K is in the second half, 
    then we could put K -= (1 << N-2) so that it is in the first half, and flip the final answer.
    
    Runtime: 32 ms, faster than 41.79% of Python3.
    Memory Usage: 14 MB, less than 100.00% of Python3.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        if K <= (2**(N-2)):
            return self.kthGrammar(N-1, K)
        return self.kthGrammar(N-1, K-2**(N-2)) ^ 1


class Solution4:
    """
    Runtime: 32 ms, faster than 41.79% of Python3 
    Memory Usage: 14.1 MB, less than 100.00% of Python3
    
    Time Complexity: O(log N), the number of binary bits in N. If logN is taken to be bounded, this can be considered to be O(1).
    Space Complexity: O(1). (In Python, bin(X) creates a string of length O(logX), which could be avoided.)
    """
    def kthGrammar(self, N: int, K: int) -> int:
        return bin(K - 1).count('1') % 2
