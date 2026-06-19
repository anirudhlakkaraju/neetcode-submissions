class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int, int> m;
        vector<vector<int>> buckets(n+1);
        vector<int> res;

        for(int i: nums){
            m[i]++;
        }

        for(auto i: m){
            buckets[i.second].push_back(i.first);
        }

        for(int i=n; i>=1; i--){
            for(int j=0; j<buckets[i].size(); j++){
                if(k==0)
                    return res;
                res.push_back(buckets[i][j]);
                k--;
            }
        }

        return res;
    }
};
