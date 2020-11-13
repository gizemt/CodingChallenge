''' Leetcode 104: Maximum Depth of Binary Tree
# Question  : Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.

# Link      : https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Runtime   : 32 ms   - 98%
# Memory    : 15.9 MB - 19%
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            l = self.maxDepth(root.left)
            r = self.maxDepth(root.right)
            return 1 + max(l, r)