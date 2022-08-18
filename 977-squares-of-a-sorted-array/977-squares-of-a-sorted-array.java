class Solution {
    public int[] sortedSquares(int[] nums) {
        for (int i = 0; i < (nums.length); i++){
            nums[i] *= nums[i];
        }
        mergesort(nums, 0, (nums.length)-1);
            
        return nums;
    }
    public static void mergesort(int[] array, int low, int high){
        int mid;
        if (low < high){
            mid = (low + high)/2;
            mergesort(array, low, mid);
            mergesort(array, mid+1, high);
            merge(array, low, mid, high);
        }


    }
    public static void merge(int[] array, int lower, int middle, int upper){
        int i = lower, j = middle+1, k = 0;
        int size = upper - lower + 1;
        int[] temp = new int[size];
        while(i <= middle && j <= upper){
            if (array[i] < array[j]){
                temp[k++] = array[i++];
            }
            else {
                temp[k++] = array[j++];
            }
        }
        while (i <= middle){
            temp[k++] = array[i++];
        }
        while (j <= upper){
            temp[k++] = array[j++];
        }
        for(k = 0; k < size; k++){
            array[k + lower] = temp[k];
        }
    }
}