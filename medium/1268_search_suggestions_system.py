"""
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with searchWord. If there are more than three products with a common
prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

Example 1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
    ["mobile","moneypot","monitor"],
    ["mobile","moneypot","monitor"],
    ["mouse","mousepad"],
    ["mouse","mousepad"],
    ["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
"""

import collections
from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        prefixes = collections.defaultdict(list)
        answer = []

        for product in products:
            for i in range(1, len(product)+1):
                prefixes[product[:i]].append(product)

        for i in range(1, len(searchWord)+1):
            suggestions = sorted(
                prefixes[searchWord[:i]]
            )[:3]
            answer.append(suggestions)

        return answer


if __name__ == '__main__':
    solutions = [
        Solution(),
        ]
    tc = ((
        ["mobile","mouse","moneypot","monitor","mousepad"],
        "mouse",
        [
            ["mobile","moneypot","monitor"],
            ["mobile","moneypot","monitor"],
            ["mouse","mousepad"],
            ["mouse","mousepad"],
            ["mouse","mousepad"]]
        ),
        (
            ["havana"],
            "havana",
            [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
        ),
        (
            ["bags","baggage","banner","box","cloths"],
            "bags",
            [
                ["baggage","bags","banner"],
                ["baggage","bags","banner"],
                ["baggage","bags"],
                ["bags"]]
        ),
    )
    for solution in solutions:
        for inp_products, search_word, exp_result in tc:
            assert solution.suggestedProducts(inp_products, search_word) == exp_result
