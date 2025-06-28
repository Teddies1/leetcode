class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashmap;
        int n = nums.size();
        vector<int> ans;

        for(int i = 0; i < n; i++){
            int difference = target - nums[i];
            if (hashmap.find(difference) != hashmap.end()){
                ans = {i, hashmap[difference]};
                return ans;
            }
            hashmap[nums[i]] = i;
        }
        return ans;
    }
};