# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    """def traversalHelper(self, root, lst = []):
        
        if not root:
            return lst
        
        self.traversalHelper(root.left, lst)
        self.traversalHelper(root.right, lst)
        lst.append(root.val)
        
        return lst
        
    def postorderTraversal(self, root):
       
        return self.traversalHelper(root)"""
        
    # recursively 
    def postorderTraversal(self, root):
        res = []
        self.dfs(root, res)
        return res
    
    def dfs(self, root, res):
        if root:
            self.dfs(root.left, res)
            self.dfs(root.right, res)
            res.append(root.val)