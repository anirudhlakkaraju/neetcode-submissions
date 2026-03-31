class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  
        n = len(s)
        l, r = 0, 0
        m = {}
        res = 0
        
        while r < n:
            
            if s[r] in m:
                l = max(m[s[r]] + 1, l)
                
            res = max(res, r-l+1)

            m[s[r]] = r
            r += 1

        return res

            
