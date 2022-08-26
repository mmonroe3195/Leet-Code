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
        
        #saving the old left and right
        if not root:
            return root
        
        new_left = root.right
        new_right = root.left
        
        if root.left:
            self.invertTree(root.left)
            
        
        if root.right:
            self.invertTree(root.right)
          
        #updating the inverted parts of the tree
        root.left = new_left
        root.right = new_right
        
        return root