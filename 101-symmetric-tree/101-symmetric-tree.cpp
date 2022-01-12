/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        return compare(root->left, root->right);
            
    }
    
    bool compare(TreeNode* l, TreeNode* r) {
    
        if(!l && !r)
            return true;
        
        else if((!l && r )|| (l && !r) || (l->val != r->val))
            return false;
        
        return compare(l->right, r-> left) && compare(l->left, r-> right);
        
        
    }
};