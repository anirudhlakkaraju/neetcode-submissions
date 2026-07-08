class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n = s1.size(), m = s2.size();

        unordered_map<char, int> m1, m2;
        for(char c: s1)
            m1[c]++;
        
        int lo = 0, hi = 0;
        while(hi<m){
            m2[s2[hi]]++;

            if(hi-lo+1==n){
                if(m1==m2)
                    return true;
                
                m2[s2[lo]]--;
                if(!m2[s2[lo]])
                    m2.erase(s2[lo]);
                
                lo++;
            }

            hi++;
        }

        return false;
    }
};
