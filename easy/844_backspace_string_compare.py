"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""

class Solution:
    """
    Runtime: 20 ms
    Memory Usage: 13.8 MB
    
    Your runtime beats 97.78 % of python3 submissions.
    """
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_stack, t_stack = [], []
        for stack_item in ((S, s_stack), (T, t_stack)):
            string_, stack_ = stack_item
            for ltr in string_:
                if ltr == "#":
                    if len(stack_) > 0:
                        stack_.pop()
                else:
                    stack_.append(ltr)
        return s_stack == t_stack


if __name__ == '__main__':
    test_cases = [
        ("ab#c", "ad#c", True),  # Both S and T become "ac"
        ("ab##", "c#d#", True),  # Both S and T become ""
        ("a##c", "#a#c", True),  # Both S and T become "c"
        ("a#c", "b", False)      # S becomes "c" while T becomes "b"
    ]
    sol = Solution()
    for case in test_cases:
        S, T, expected_result = case
        assert sol.backspaceCompare(S, T) == expected_result
