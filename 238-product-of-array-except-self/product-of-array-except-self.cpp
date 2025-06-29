class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> prefix_sum(n, 1);
        vector<int> postfix_sum(n, 1);
        vector<int> ans;
        /*
        [1, 1, 2, 6]
        [24, 12, 4, 1]
        
        */
        for (int i = 1; i < n; i++){
            prefix_sum[i] = prefix_sum[i-1] * nums[i-1];
        }

        for (int i = n-2; i >= 0; i--){
            postfix_sum[i] = postfix_sum[i+1] * nums[i+1];
        }

        for (int i = 0; i < n; i++){
            ans.push_back(prefix_sum.at(i) * postfix_sum.at(i));
        }

        return ans;
    }
};
