class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        int zero_index = 0;
        for (int i = 0; i < n; i++){
            if (nums[i] != 0){
                swap(nums[i], nums[zero_index]);
                zero_index++;
            }
        }
    }
};