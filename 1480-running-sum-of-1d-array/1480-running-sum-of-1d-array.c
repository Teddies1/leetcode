/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* runningSum(int* nums, int numsSize, int* returnSize){
    *returnSize = numsSize;
    int count = 0;
    int *array = (int*)malloc(sizeof(int) * *returnSize);
    
    for (int i = 0; i < *returnSize; i++){
        count += nums[i];
        array[i] = count;
    }
    return array;
    
}