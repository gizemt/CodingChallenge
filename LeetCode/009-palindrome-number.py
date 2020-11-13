''' Leetcode 009: palindrome-number
# Question  : Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
Follow up: Could you solve it without converting the integer to a string?

# Link      : https://leetcode.com/problems/palindrome-number/
# Runtime   : 36 ms   - 97%
# Memory    : 11.8 MB - %
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            if x == int(str(x)[-1::-1]):
                return True
            else:
                return False