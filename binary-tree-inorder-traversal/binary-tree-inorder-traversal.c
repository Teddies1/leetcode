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
void insert(struct TreeNode *root, int *array, int* size){
    if (root == NULL){
        return;
    }
    
    insert(root->left, array, size);
    array[(*size)++] = root->val;
    insert(root->right, array, size);
}

int* inorderTraversal(struct TreeNode* root, int* returnSize){
    int *array = malloc(sizeof(int) * 100);
    int *size = 0;
    
    insert(root, array, &size);
    *returnSize = size;

    return array;
    
    
    
}