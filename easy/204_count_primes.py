"""
Count the number of prime numbers less than a non-negative number, n.

a number is prime, we need to check if it is not divisible by any number less than n.
"""


class Solution:
    """
    Sieve of Eratosthenes (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
    https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif

    Algorithm idea:
    0. Allocate store (sieve), 1 and 0 are not primes and we mark them as False,
                               2 and onwards are "unknown" - mark as True for a while
    1. Start from 2 (is prime number) - skip the num, but also loop over the list until the end and mark as
    False multiplications of two (as they all are divisible by two - they not primes): 4, 6, 8, 10, 12, 14...
    2. Repeat step one for next number in the list (its 3): 6, 9, 12, 15, 18, 21...
    2.1 then do the same with 4 (we marked it as False when worked with 2), etc.): 8, 12, 16, 20, 24...
    3. The result will be number of cells left as True - those nums are prime numbers
    Note. As an optimization, we do not loop all the nums, we just need to verify until "i <= sqrt(num)"

    Runtime: 444 ms, faster than 73.42% of Python3.
    Memory Usage: 37.2 MB, less than 28.76% of Python3.
    Time complexity: O(n log log n)
    Space complexity: O(n)

    i*i seems works faster than pow 2 of i:
    "timeit 10*10
    6.86 ns ± 0.0197 ns per loop (mean ± std. dev. of 7 runs, 100000000 loops each)
    timeit 10**2
    6.86 ns ± 0.0378 ns per loop (mean ± std. dev. of 7 runs, 100000000 loops each)
    "
    """

    def countPrimes(self, n: int) -> int:
        sieve = [False] * 2 + [True] * (n - 2)  # 0 and 1 are not primes, so marked as False
        i = 2
        while i * i < n:  # i <= sqrt(num)
            if sieve[i]:
                for j in range(2 * i, n, i):
                    sieve[j] = False
            i += 1
        return sieve.count(True)


class Solution2:
    """
    Take advantage of the primes already generated.

    Time complexity: O(n**2)
    Space complexity: O(n)

    Runtime: 3300 ms, faster than 9.28% of Python3 online submissions for Count Primes.
    Memory Usage: 19.1 MB, less than 96.12% of Python3 online submissions for Count Primes.
    """

    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [2]
        for i in range(3, n, 2):
            for p in primes:
                if p * p > i:
                    primes.append(i)
                    break
                if not i % p:
                    break
        return len(primes)


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    tc = (
        (10, 4),  # Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
        (0, 0),
        (1, 0),
        (3, 1),  # 2 is a prime number
        (10000, 1229)
    )
    for s in solutions:
        for num, exp_count in tc:
            res = s.countPrimes(num)
            assert res == exp_count, f'{s.__class__.__name__}: For num {num} expected {exp_count}, got {res}'
