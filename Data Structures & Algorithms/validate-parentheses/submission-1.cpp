class Solution {
public:
    bool isValid(string s) {
        int n = s.size();
        stack<char> st;
        unordered_map<char, char> m;
        m['['] = ']';
        m['{'] = '}';
        m['('] = ')';

        for(char c:s){
            if(!st.empty() && m[st.top()]==c)
                st.pop();
            else
                st.push(c);
        }

        return st.empty();
    }
};
