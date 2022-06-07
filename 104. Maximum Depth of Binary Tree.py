# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def recurse(node):
            if node is None:
                return 0
            
            if node.left is None and node.right is None:
                return 1
            
            return max(recurse(node.left)+1, recurse(node.right)+1)
        
        return recurse(root)
        