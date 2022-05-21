

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortArrayByParity(int* nums, int numsSize, int* returnSize){
    *returnSize = numsSize;
    int *array = (int*)malloc(sizeof(int) * *returnSize);
    int j = 0; int i;
    
    for ( i = 0; i < numsSize; i++){
        if (nums[i] % 2 == 0){
            array[j] = nums[i];
            j++;
        }
    }
    for ( i = 0; i < numsSize; i++){
        if (nums[i] % 2 == 1){
            array[j] = nums[i];
            j++;
        }
    }
    
    
    
    
    return array;
}