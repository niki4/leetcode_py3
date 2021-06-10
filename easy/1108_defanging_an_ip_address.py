"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

Constraints:
    The given address is a valid IPv4 address.
"""


class Solution:
    """
    Python str type built-in method (creates a new string with replaced elements)

    Runtime: 28 ms, faster than 77.82% of Python3
    Memory Usage: 14.1 MB, less than 85.53% of Python3

    Time: O(1) as we deal with fixed size address every time. We'd have O(n) if the size of address would be unknown.
        Here is also pretty cool analysis on .replace() method: "The worst case is O(n*(m1 + m2/m1)) where n is the
        length of the string, m1 is the length of the searched for string and m2 is the length of the replacement."
        https://stackoverflow.com/a/66164223
    Space: O(n) where n is the size of the address.
           Since we have fixed size address then additional space is also constant so O(1).
    """

    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


class Solution2:
    """
    String concatenation (SC) with replacing "." char by "[.]"
    SC is a slow operation.

    Runtime: 48 ms, faster than 6.38% of Python3
    Memory Usage: 14.2 MB, less than 62.12% of Python3

    Time complexity:  in case string concatenation requires all characters to be copied, this is a O(N+M) operation
    (where N and M are the sizes of the input strings). M appends of the same word will trend to O(M^2) time.
    https://stackoverflow.com/a/37133870
    """

    def defangIPaddr(self, address: str) -> str:
        result = ""
        for char in address:
            result += "[.]" if char == "." else char
        return result


class Solution3:
    """
    str.split() creates a list of elements between specified separator, then
    str.join() builds a string (from a given list) in a single pass.

    Runtime: 64 ms, faster than 6.38% of Python3
    Memory Usage: 13.9 MB, less than 99.59% of Python3

    Time complexity: O(N) (where N is the total length of the output).
    """

    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split("."))


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
    tc = (
        ("1.1.1.1", "1[.]1[.]1[.]1"),
        ("255.100.50.0", "255[.]100[.]50[.]0"),
    )
    for sol in solutions:
        for inp_address, exp_address in tc:
            assert sol.defangIPaddr(inp_address) == exp_address
