class Solution {
public:

    string encode(vector<string>& strs) {
        int n = strs.size();
        string encoded;

        for(int i=0; i<n; i++){
            int m = strs[i].size();
            encoded += to_string(m) + "#" + strs[i];
        }
        cout << encoded << endl;
        return encoded;
    }

    vector<string> decode(string s) {
        int n = s.size();
        vector<string> decoded;

        int i=0;
        while(i<n){
            // get char count
            string num;
            while(s[i] != '#'){
                num += s[i];
                i++;
            }
            int count = stoi(num);

            // skip the '#'
            i += 1;

            int m = i+count;
            decoded.push_back(s.substr(i, count));
            i += count;
        }

        return decoded;
    }
};
