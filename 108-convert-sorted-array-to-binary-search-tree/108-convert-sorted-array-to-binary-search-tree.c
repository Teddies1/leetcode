/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* binsearch(int start, int end, int* nums){
    struct TreeNode *root = malloc(sizeof(struct TreeNode));
    int mid = (start + end)/2;
    if (start > end){
        return NULL;
    }
    root->val = nums[mid];
    root->left = binsearch(start, mid-1, nums);
    root->right = binsearch(mid+1, end, nums);
    
    
    return root;
    
}

struct TreeNode* sortedArrayToBST(int* nums, int numsSize){
    
    return binsearch(0, numsSize-1, nums);
}