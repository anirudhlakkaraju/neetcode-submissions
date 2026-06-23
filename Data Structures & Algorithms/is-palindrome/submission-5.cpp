class Solution {
public:
    bool isPalindrome(string s) {
        int n = s.size();
        int lo = 0, hi = n-1;

        while(lo<=hi){
            while(lo<n &&(!isalnum(s[lo]) || s[lo]==' ')){
                lo++;
            }
            while(hi>=0 && (!isalnum(s[hi]) || s[hi]==' ')){
                hi--;
            }
            if(tolower(s[hi]) != tolower(s[lo]))
                return false;
            lo++;
            hi--;
        }

        return true;
    }
};
