
int max(int a, int b){
    return a > b ? a : b;
}
int maxSubArray(int* nums, int numsSize){
    int newsum = 0x80000000;
    int currentsum = 0;
      
    for (int i = 0; i < numsSize; i++){
        currentsum += nums[i];
        newsum = max(newsum, currentsum);
        currentsum = max(currentsum, 0);
    }
    return newsum;
}