''' Leetcode 020: valid-parentheses
# Question  : Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

# Link      : https://leetcode.com/problems/valid-parentheses/
# Runtime   : 36 ms   - 17%
# Memory    : 13.9 MB - 91%
'''

class Solution:
    def isValid(self, s: str) -> bool:
        open_pars = []
        par_pairs = {'(':')', '{':'}', '[':']'}
        for p in s:
            if p in par_pairs:
                open_pars.append(par_pairs[p])
            elif not open_pars:
                return False
            else:
                o = open_pars.pop()
                if o != p:
                    return False
        return not open_pars