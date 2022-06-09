/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int max(int a, int b){
    return a > b ? a : b;
}
int height(struct TreeNode *root){
    if (root == NULL){
        return 0;
    }
    int left = 1 + height(root->left);
    int right = 1 + height(root->right);
    
    return max(left, right);
}

bool isBalanced(struct TreeNode* root){
    if (root == NULL){
        return true;
    }
    
    int left = height(root->left);
    int right = height(root->right);
    
    int diff = left-right;
    
    if (diff > 1 || diff < -1){
        return false;
    }
    if (isBalanced(root->right) == false || isBalanced(root->left) == false){
        return false;
    }
    
    return true;
}