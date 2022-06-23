# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def iot_helper(self, root, arr):
        if root.left:
            self.iot_helper(root.left, arr)

        arr.append(root.val)
        
        if root.right:
            self.iot_helper(root.right, arr)
            
        return arr
        
    def inorderTraversal(self, root):
        arr = []
        if not root:
            return arr

        return self.iot_helper(root, arr)
   
            
        