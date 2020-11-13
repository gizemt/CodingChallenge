#### Leetcode 101: Symmetric Tree ####
# Question  : Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# Link      : https://leetcode.com/problems/symmetric-tree/
# Runtime   : 28 ms   - 94%
# Memory    : 14.3 MB - 47%
#### Leetcode 101: Symmetric Tree ####

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.isMirror(root, root)
        
    def isMirror(self, node1, node2):
        if (node1 != None and node2 == None) or (node1 == None and node2 != None):
            return False
        elif node1==None and node2==None:
            return True
        elif node1.val != node2.val:
            return False
        else:
            return self.isMirror(node1.left, node2.right) and self.isMirror(node1.right, node2.left)