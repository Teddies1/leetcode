/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int nodecount(struct TreeNode *root){
    if (root == NULL){
        return 0;
    }
   
    return 1 + nodecount(root->left) + nodecount(root->right);
}
void insert(struct TreeNode* root, int* array, int* i){
    if (root == NULL){
        return;
    }
    
    
    array[(*i)] = root->val;
    (*i)++;
    insert(root->left, array, i);
    insert(root->right, array, i);
}
int* preorderTraversal(struct TreeNode* root, int* returnSize){
    *returnSize = nodecount(root);
    int *array = (int*)malloc(sizeof(int) * *returnSize);
    
    int* index = 0;
    insert(root, array, &index);
    
    return array;
    
    
}