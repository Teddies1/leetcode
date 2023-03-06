class Solution {
    public int[] productExceptSelf(int[] nums) {
        int size = nums.length;
        int[] prefix = new int[size];
        int[] suffix = new int[size];
        int[] res = new int[size];
        
        /*
        prefix[1, 1, 2, 6]
        suffix[24, 12, 4, 1]
        */
        prefix[0] = 1;
        suffix[size-1] = 1;
        for (int i = 1; i < size; i++){
            prefix[i] = prefix[i-1] * nums[i-1];
            System.out.println(prefix[i]);
        }
        for (int i = size-2; i >= 0; i--){
            suffix[i] = suffix[i+1] * nums[i+1];
            System.out.println(suffix[i]);
        }
        for (int i = 0; i < size; i++){
            res[i] = suffix[i] * prefix[i];
        }
        return res;
    }
}