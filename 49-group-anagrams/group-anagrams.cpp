class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hashmap;
        vector<vector<string>> ans;

        for(string s: strs){
            string sorted_str = s;
            sort(sorted_str.begin(), sorted_str.end());
            hashmap[sorted_str].push_back(s);

        }
        for(auto& key_value: hashmap){
            vector<string> string_array = key_value.second;
            ans.push_back(string_array);
        }
        return ans;
    }
};