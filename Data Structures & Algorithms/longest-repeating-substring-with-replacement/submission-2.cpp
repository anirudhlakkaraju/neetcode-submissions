class Solution {
public:

    int mxChar(unordered_map<char, int> m) {
        int res = 0;
        for(auto i:m){
            res = max(res, i.second);
        }

        return res;
    }

    int characterReplacement(string s, int k) {
        int n = s.size();
        unordered_map<char, int> m;

        int res = 0, lo = 0, hi = 0;

        while(hi<n){
            m[s[hi]]++;

            while(lo<hi && (hi-lo+1 - mxChar(m) > k)){
                m[s[lo]]--;
                lo++;
            }

            res = max(res, hi-lo+1);
            hi++;
        }


        return res;
    }
};
