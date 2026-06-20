class Solution {
public:

    string encode(vector<string>& strs) {
        int n = strs.size();
        string res;

        for(int i=0; i<n; i++){
            res += to_string(strs[i].size());
            res += '#';
            res += strs[i];
        }
        // cout << res << endl;
        return res;
    }

    vector<string> decode(string s) {
        int n = s.size();
        vector<string> res;

        int i = 0;
        while(i<n){
            // get the len first
            string l;
            while(s[i]!='#'){
                l += s[i];
                i++;
            }

            int len = stoi(l), j = i+1;
            // cout << j << endl;
            string str;
            for(; j<i+len+1; j++){
                str += s[j];
            }
            res.push_back(str);
            i = j;
        }
        
        return res;
    }   
};
