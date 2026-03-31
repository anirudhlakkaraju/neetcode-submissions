class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s + "."
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        
        if len(s) == 0:
            return res

        t = ""
        for c in s:
            if c == '.':
                res.append(t)
                t = ""
            else:
                t += c

        return res
            

