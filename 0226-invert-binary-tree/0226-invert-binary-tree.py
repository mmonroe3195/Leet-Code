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
        if not root:
            return root
        
        #inverting the current level
        new_left, new_right = root.right, root.left        
        root.left, root.right = new_left, new_right
        
        #inverting the children recersively
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root