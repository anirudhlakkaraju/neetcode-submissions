class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map<int, int> m;

        for(int i=0; i<n; i++){
            m[nums[i]] = i;
        }

        for(int i=0; i<n; i++){
            int diff = target-nums[i];

            if(m.find(diff) != m.end()){
                if(m[diff] != i){
                    return {i, m[diff]};
                }
            }
        }

        return {};
    }
};
