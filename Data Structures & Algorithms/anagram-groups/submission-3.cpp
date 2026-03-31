class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        int n = strs.size();
        unordered_map<string, vector<string>> m;
        vector<vector<string>> res;

        for(int i=0; i<n; i++){
            vector<int> count(26, 0);
            for(char c:strs[i]){
                count[c-'a']++;
            }

            string key = to_string(count[0]);
            for(int i=1; i<26; i++){
                key += ',' + to_string(count[i]);
            }
            
            m[key].push_back(strs[i]);
        }

        for(auto it=m.begin(); it!=m.end();it++){
            res.push_back(it->second);
        }
        
        return res;
    }
};
