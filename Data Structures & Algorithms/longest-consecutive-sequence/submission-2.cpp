class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, int> m;

        for(int i:nums){
            m[i]++;
        }

        int res = 0;
        for(int i=0; i<n; i++){
            // If current num is start of seq 
            // i.e., there is not prev element
            if(m.find(nums[i]-1)==m.end()){
                int len = 1;
                while(m.find(nums[i]+len)!=m.end()){
                    len++;
                }
                res = max(res, len);
            }
        }

        return res;
    }
};
