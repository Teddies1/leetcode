/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


struct TreeNode* searchBST(struct TreeNode* root, int val){
    if (root == NULL || val == root->val){
        return root;    
    }
    if (val > root->val){
        return searchBST(root->right, val);
    }
    
    return searchBST(root->left, val);
}