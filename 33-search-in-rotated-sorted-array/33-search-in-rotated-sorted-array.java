class Solution {
    public int search(int[] nums, int target) {
        return helper(nums, 0, nums.length-1, target);
    }
    public int helper(int[] array, int start, int end, int target){
        int mid;
        while (start <= end){
            mid = start + (end - start) / 2;
            if (target == array[mid]){
                return mid;
            }
            /*
                if the mid value is greater than the first element, 
                it means that the mid value is in the left sorted portion.
                
                then we check the target, if the target is smaller than the first element,
                or greater than the mid value, then the answer is in the right half.
                
                else its in the left half
            */
                
            else if (array[start] <= array[mid]){
                if (target < array[start] || target > array[mid]){
                    start = mid+1;
                }
                else{
                    end = mid-1;
                }
            }
            /*
                if the mid value is smaller than the last element,
                it means the mid value is in the right sorted portion.
                
                if the target is larger than the last element, or is smaller than the mid value
                then the answer is in the left half
                
                else its in the right half
            */
            else{
                if (target > array[end] || target < array[mid]){
                    end = mid-1;
                }
                else{
                    start = mid+1;
                }
            }
        }
        return -1;
    }
}