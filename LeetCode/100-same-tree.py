''' Leetcode 100: same-tree
# Question  : Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
# Link      : https://leetcode.com/problems/same-tree/
# Runtime   : 28 ms   - 80%
# Memory    : 14.1 MB - 59%
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val == q.val:
            if not self.isSameTree(p.left, q.left):
                return False
            elif not self.isSameTree(p.right, q.right):
                return False
            else:
                return True
        else:
            return False