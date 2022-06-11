/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


bool isSameTree(struct TreeNode* p, struct TreeNode* q){
    if (p == NULL && q == NULL) {
        return true;
    }
    if (q == NULL || p == NULL || q->val != p->val){
        return false;
    }
    bool left = isSameTree(p->left, q->left);
    bool right = isSameTree(p->right, q->right);
    
    
    return left && right;
}