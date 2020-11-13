''' Leetcode 006: zigzag-conversion
# Question  : The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

# Link      : https://leetcode.com/problems/zigzag-conversion/
# Runtime   : 68 ms   - 33%
# Memory    : 11.8 MB - %
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        zigzag = ''
        if numRows > 1:
            for i in range(numRows):
                for j in range(0, len(s)+2*(numRows-1), 2*(numRows-1)):
                    if i == 0:
                        if j < len(s):
                            zigzag += s[j]
                    elif i == numRows-1 or j == 0:
                        if i + j < len(s):
                            zigzag += s[j+i]
                    else:
                        if j - i < len(s):
                            zigzag += s[j-i]
                        if i + j < len(s):
                            zigzag += s[j+i]
        elif numRows == 1:
            zigzag = s
                
        return zigzag