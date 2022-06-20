
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
        else{
            leftsum = sum(nums, 0, i);
        }
        if (i == numsSize){
            rightsum = 0;
        }
        else{
            rightsum = sum(nums, i+1, numsSize);
        }
        if (rightsum == leftsum){
            return i;
        }
        printf("%d ", leftsum);
        printf("%d\n", rightsum);        
    }
    return -1;
}