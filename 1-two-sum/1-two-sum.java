class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hash = new HashMap<Integer,Integer>();
        int[] res = new int[2];
        int remain;
        for (int i = 0; i < nums.length; i++){
            remain = target - nums[i];
            if (hash.containsKey(remain)){
                res[0] = i;
                res[1] = hash.get(remain);
            }
            hash.put(nums[i], i);
        }
        return res;
    }
}