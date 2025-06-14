class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hashmap = new HashMap<>();
        int n = nums.length;
        int[] ans = new int[2];
        for (int i = 0; i < n; i++){
            int difference = target - nums[i];
            if (hashmap.containsKey(difference)){
                ans[0] = hashmap.get(difference);
                ans[1] = i;
                return ans;
            }
            hashmap.put(nums[i], i);
        }

        return ans;
    }
}