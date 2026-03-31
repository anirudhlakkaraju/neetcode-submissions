class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)

        if m > n:
            return ""

        m1 = {}
        for c in t:
            m1[c] = m1.get(c, 0) + 1

        need, have = len(m1), 0
        res = ""
        l = 0
        m2 = {}
        for r in range(n):
            c = s[r]

            out = c + f", m2: {m2}"
            # expand window
            if c not in m1:
                out += ", l: " + str(l)+ ", r: " + str(r)
                print(out)
                continue

            m2[c] = m2.get(c, 0) + 1
            
            if m2[c] == m1[c]:
                have += 1

            # once we get a valid window
            while have == need:

                # update res
                if res == "" or r-l+1 < len(res):
                    res = s[l:r+1]
                
                # shrink window
                if s[l] in m2:
                    m2[s[l]] -= 1
                    if m2[s[l]] < m1[s[l]]:
                        have -= 1
                    if m2[s[l]] == 0:
                        m2.pop(s[l])

                l += 1 

            out += ", l: " + str(l)+ ", r: " + str(r)
            print(out + ", res:" + res)
        return res