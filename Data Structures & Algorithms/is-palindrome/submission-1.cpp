class Solution {
public:
    bool isPalindrome(string s) {

        string t;
        for(int i=0; i<s.size(); i++) {
            if(isalnum(s[i]))
                t.push_back((char)tolower(s[i]));
        }

        int n = t.size(), lo = 0, hi = n-1;
        while(lo<hi){
            if(t[lo]!=t[hi])
                return false;
            lo++;
            hi--;
        }

        return true;
    }
};
