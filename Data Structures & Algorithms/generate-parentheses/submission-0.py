class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def f(s, op, cl):
            if op == n and cl == n:
                res.append(s)
                return
            
            if op < n:
                f(s + '(', op + 1, cl)
            if op > cl:
                f(s + ')', op, cl + 1)
        
        f("", 0, 0)

        return res