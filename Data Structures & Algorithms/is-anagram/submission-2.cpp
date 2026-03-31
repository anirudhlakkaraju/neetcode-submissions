class Solution {
public:
    bool isAnagram(string s, string t) {
        int n = s.size(), m = t.size();

        if(n != m)
            return false;

        unordered_map<char, int> ms, mt;

        for(int i=0; i<n; i++){
            ms[s[i]]++;
        }

        for(int i=0; i<m; i++){
            mt[t[i]]++;
        }

        for(int i=0; i<n; i++){
            if(ms[s[i]] != mt[s[i]]) 
                return false;
        }

        return true;
    }
};
