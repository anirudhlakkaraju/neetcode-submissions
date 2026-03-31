class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)

        if m > n:
            return ""

        mt, ms = {}, {}
        for c in t:
            mt[c] = mt.get(c, 0) + 1
        
        need, have = len(mt), 0
        lo, hi = 0, 0
        res = ""
        while hi < n:
            c = s[hi]

            # update map
            if c in mt:
                ms[c] = ms.get(c, 0) + 1
                if ms[c] == mt[c]:
                    have += 1
            
            # valid window
            while have == need:
                if len(res) == 0 or hi-lo+1 < len(res):
                    res = s[lo:hi+1]
                
                # shrink window
                c = s[lo]
                if c in mt:
                    ms[c] -= 1
                    if ms[c] < mt[c]:
                        have -= 1
                    if ms[c] == 0:
                        del ms[c]
                
                lo += 1
            
            hi += 1

        return res