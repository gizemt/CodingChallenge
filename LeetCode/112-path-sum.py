''' Leetcode 112: path-sum
# Question  : Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

# Link      : https://leetcode.com/problems/path-sum/
# Runtime   : 40 ms   - 82%
# Memory    : 15.8 MB - 50%
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        elif not root.left and not root.right and root.val == sum:
            return True        
        else:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)