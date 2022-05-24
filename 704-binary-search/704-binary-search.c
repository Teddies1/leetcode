int helper(int start, int end, int target, int* array){
    if (start > end){
        return -1;
    }
    int mid = (end + start)/2;
    
    if (array[mid] == target){
        return mid;
    }
    if (target > array[mid]){
        return helper(mid+1, end, target, array);
    }
    if (target < array[mid]){
        return helper(start, mid-1, target, array);
    }
    return -1;
    
}

int search(int* nums, int numsSize, int target){
    
    return helper(0,numsSize-1,target,nums);
}