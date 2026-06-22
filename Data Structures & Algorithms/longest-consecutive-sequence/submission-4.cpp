class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, int> m;
        int res = 0;

        for(int i:nums)
            m[i]++;

        for(int i=0; i<n; i++){
            // start of seq detected
            if(m.find(nums[i]-1)==m.end()){
                int len = 0;
                while(m.find(nums[i]+len)!=m.end()){
                    len++;
                }
                res = max(res, len);
            }
        }
        
        return res;
    }
};
