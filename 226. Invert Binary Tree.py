# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def recurse(node):
            if node is None:
                return None
            
            if node.left is None and node.right is None:
                return node
            
            node.left, node.right = node.right, node.left
            recurse(node.left)
            recurse(node.right)
            
            return node
            
            
        return recurse(root)
        