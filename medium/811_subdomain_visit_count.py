"""
A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level,
we have "leetcode.com" and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com",
 we will also visit the parent domains "leetcode.com" and "com" implicitly.

A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep is the number of
visits to the domain and d1.d2.d3 is the domain itself.

For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that discuss.leetcode.com was visited 9001 times.
Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain in the input.
You may return the answer in any order.

Example 1:
Input: cpdomains = ["9001 discuss.leetcode.com"]
Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
Explanation: We only have one website domain: "discuss.leetcode.com".
As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.

Example 2:
Input: cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation: We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times.
For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.

Constraints:
    1 <= cpdomain.length <= 100
    1 <= cpdomain[i].length <= 100
    cpdomain[i] follows either the "repi d1i.d2i.d3i" format or the "repi d1i.d2i" format.
    repi is an integer in the range [1, 104].
    d1i, d2i, and d3i consist of lowercase English letters.
"""

import collections
from typing import List

class Solution:
    """
    Time/Space complexity: O(n)
    """
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        seen = collections.defaultdict(int)
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ", maxsplit=1)
            seen[domain] += int(count)

            for i, ch in enumerate(domain):
                if ch == ".":
                    seen[domain[i+1:]] += int(count)


        return [" ".join(str(i) for i in item[::-1]) for item in seen.items()]


class Solution2:
    """
    Time complexity: O(n*k)
    """
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result = []
        domain_counter = collections.defaultdict(int)

        for domain_stat in cpdomains:
            visits, fqdn = domain_stat.split()  # FQDN - Fully Qualified Domain Name, e.g. discuss.leetcode.com
            visits = int(visits)
            domain_parts = fqdn.split(sep=".")

            for i in range(len(domain_parts)):
                domain = ".".join(domain_parts[i:])
                domain_counter[domain] += visits

        for domain, visits in domain_counter.items():
            result.append(f"{visits} {domain}")

        return result


if __name__ == '__main__':
    solutions = [
        Solution(),
        Solution2(),
    ]
    tc = (
        (["9001 discuss.leetcode.com"],
        ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]),
        (["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"],
        ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]),
    )
    for sol in solutions:
        for inp_cpdomains, exp_res in tc:
            res = sol.subdomainVisits(inp_cpdomains)
            assert sorted(res) == sorted(exp_res), f'{sorted(res)} != {sorted(exp_res)}'
