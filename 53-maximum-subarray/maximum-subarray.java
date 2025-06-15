class Solution {
    public int maxSubArray(int[] nums) {
        int max_sum = Integer.MIN_VALUE;
        int curr_sum = 0;
        for (int num: nums){
            curr_sum += num;
            max_sum = Math.max(max_sum, curr_sum);
            curr_sum = Math.max(curr_sum, 0);

        }
        return max_sum;
    }
}