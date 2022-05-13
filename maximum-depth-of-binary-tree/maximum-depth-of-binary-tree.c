/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int max(int a, int b){
    return (a > b) ? a : b;
}

int maxDepth(struct TreeNode* root){
    int left, right;
    
    if (root == NULL){
        return 0;
    }
    
    left = 1 + maxDepth(root->left);
    right = 1 + maxDepth(root->right);
    
    return max(left, right);
    

}