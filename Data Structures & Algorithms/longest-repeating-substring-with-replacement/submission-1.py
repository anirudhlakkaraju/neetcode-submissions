class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l, r = 0, 0
        m = {}
        res = 0

        while r < n:

            m[s[r]] = m.get(s[r], 0) + 1

            max_freq = 0
            for val in m.values():
                max_freq = max(max_freq, val)

            while (r - l + 1) - max_freq > k:
                m[s[l]] -= 1
                if m[s[l]] == 0:
                    m.pop(s[l])
                l += 1


            res = max(res, r - l + 1)
            r += 1

        return res
