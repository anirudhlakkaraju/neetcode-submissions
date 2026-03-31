class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        st = []
        res = 0

        for i in range(n):
            start = i
            while st and heights[i] < st[-1][1]:
                start = st[-1][0]
                res = max(res, st[-1][1] * (i - st[-1][0]))
                st.pop()

            st.append((start, heights[i]))
        
        while st:
            res = max(res, st[-1][1] * (n-st[-1][0]))
            st.pop()

        return res