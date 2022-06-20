
int sum(int* array, int start, int end){
    int sum = 0;
    for (int i = start; i < end; i++){
        sum += array[i];
    }
    return sum;
}
int pivotIndex(int* nums, int numsSize){
    int leftsum, rightsum;
    for (int i = 0; i < numsSize; i++){
        if (i == 0){
            leftsum = 0;
        }
        if (i == numsSize){
            rightsum = 0;
        }
        rightsum = sum(nums, i+1, numsSize);
        leftsum = sum(nums, 0, i);
        if (rightsum == leftsum){
            return i;
        }
    }
    return -1;
}