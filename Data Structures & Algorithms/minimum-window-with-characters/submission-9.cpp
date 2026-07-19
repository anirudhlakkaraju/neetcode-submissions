class Solution {
public:
    bool contains(unordered_map<char, int> ms, unordered_map<char, int> mt){
        for(auto it:mt){
            if(ms[it.first] < it.second)
                return false;
        }
        return true;
    }

    string minWindow(string s, string t) {
        int n = s.size(), m = t.size();

        if(n < m)
            return "";

        unordered_map<char, int> ms, mt;

        for(char c: t)
            mt[c]++;
        
        int lo = 0, hi = 0, len = n;
        string res;

        while(hi<n){
            ms[s[hi]]++;

            while(contains(ms, mt)){
                if(hi-lo+1 <= len){
                    len = hi-lo+1;
                    res = s.substr(lo, len);
                }
                ms[s[lo]]--;
                lo++;
            }

            hi++;
        }

        return res;
    }
};
