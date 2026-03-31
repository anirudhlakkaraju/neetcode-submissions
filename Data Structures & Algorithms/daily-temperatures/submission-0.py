class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = []
        res = [0] * n

        for i in range(n - 1, -1, -1):

            # Find the next greatest element
            while st and st[-1][0] <= temperatures[i]:
                st.pop()
            
            # If present, set res
            if st:
                res[i] = st[-1][1] - i

            st.append((temperatures[i], i))
        
        return res