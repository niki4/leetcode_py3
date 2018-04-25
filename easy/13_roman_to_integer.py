""" https://leetcode.com/problems/roman-to-integer/description/ """


# Runtime: 172 ms (Your runtime beats 25.02 % of python3 submissions.)
# Status: Accepted (https://leetcode.com/submissions/detail/149837899/)
class Solution:
    def romanToInt(self, s: str):
        """
        :type s: str
        :rtype: int
        """
        if not isinstance(s, str):
            return ValueError

        numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        input = [numerals[i] for i in list(s)]

        result = int()
        i = 0

        while (i < len(s)):
            s1 = input[i]

            if (i + 1 < len(s)):
                s2 = input[i+1]
                if (s1 >= s2):
                    result = result + s1
                    i = i + 1
                else:
                    result = result + s2 - s1
                    i = i + 2
            else:
                result = result + s1
                i = i + 1
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.romanToInt('MMMDCCCCLXXXXVIIII'))  # Expected: 3999
    print(sol.romanToInt('MCMXCVI'))             # Expected: 1996    (1000 900 90 6)
