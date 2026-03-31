class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        m = {')': '(', '}': '{', ']': '['}
        
        for i in range(len(s)):
            if st and s[i] in m and st[-1] == m[s[i]]:
                st.pop()
            else:
                st.append(s[i])

        return len(st) == 0