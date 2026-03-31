class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int, int> m1;
        unordered_map<int, vector<int>> m2;
        for(int i=0; i<n; i++){
            m1[nums[i]]++;
        }

        for(auto &p:m1){
            m2[p.second].push_back(p.first);
        }

        vector<vector<int>> buckets(n+1);
        for(int i=1; i<=n; i++){
            if(m2.find(i)!=m2.end()){
                buckets[i] = m2[i];
            }
        }

        vector<int> res;
        for(int i=n; i>=1; i--){
            for(int j=0; j<buckets[i].size(); j++){
                if(k<1)
                    return res;
                res.push_back(buckets[i][j]);
                k--;
            }
        }

        return res;
    }
};
