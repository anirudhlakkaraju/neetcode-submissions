class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        unordered_map<char, int> m;
        int res = 0;

        int lo = 0, hi = 0;
        while(hi<n){
            while(m[s[hi]]>0){
                // cout << "   s[hi]:" << s[hi] << " m[s[hi]]:" << m[s[hi]] << endl;
                m[s[lo]]--;
                lo++;
            }
            // cout << "lo: " << lo << " hi:" << hi << endl;

            m[s[hi]]++;
            res = max(res, hi-lo+1);
            hi++;
        }

        return res;
    }
};
