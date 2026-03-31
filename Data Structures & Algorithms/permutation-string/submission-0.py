class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m1 = {}
        for c in s1:
            m1[c] = m1.get(c, 0) + 1
        
        n, m = len(s1), len(s2)
        l = 0
        m2 = {}
        for r in range(m):
            m2[s2[r]] = m2.get(s2[r], 0) + 1

            if r-l+1 > n:
                m2[s2[l]] -= 1
                if m2[s2[l]] == 0:
                    m2.pop(s2[l])
                l += 1

            if m1 == m2:
                return True
        
        return False
