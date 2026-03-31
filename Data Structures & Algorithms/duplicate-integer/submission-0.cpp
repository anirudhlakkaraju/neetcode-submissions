class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, bool> m;

        for(int i=0; i<n; i++){
            if(m[nums[i]]) {
                return true;
            }
            m[nums[i]] = true;
        }

        return false;
    }
};