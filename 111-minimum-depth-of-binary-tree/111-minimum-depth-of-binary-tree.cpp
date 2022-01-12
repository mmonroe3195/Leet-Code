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
    int minDepth(TreeNode* root) {
        
        if(!root)
            return 0;
        
        size_t lheight = minDepth(root->left) + 1;
        size_t rheight = minDepth(root->right) + 1;
        
        if((lheight < rheight && lheight != 1) || rheight == 1)
            return lheight;
        
        
        return rheight;
    }
};

