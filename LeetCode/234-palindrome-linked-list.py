''' Leetcode 234: palindrome-linked-list
# Question  : Given a singly linked list, determine if it is a palindrome.

# Link      : https://leetcode.com/problems/palindrome-linked-list/
# Runtime   : 60 ms   - 97%
# Memory    : 24.1 MB - 59%
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        forward = []
        while head:
            forward.append(head.val)
            head = head.next
        backward = [forward[i] for i in range(len(forward)-1,-1,-1)]
        return backward == forward