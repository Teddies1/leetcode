/*
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
    return helper(start, mid-1, target, array);
    
}
*/
int search(int* nums, int numsSize, int target){
    //return helper(0,numsSize-1,target,nums);
    
    int start = 0, end = numsSize-1;
    int mid;
    
    while(start <= end){
        mid = (start + end)/2;
        if (nums[mid] == target){
            return mid;
        }
        if (nums[mid] < target){
            start = mid + 1;
        }
        if (nums[mid] > target){
            end = mid - 1;
        }
    }
    
    return -1;
    
    
}