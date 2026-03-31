class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        st = []
        res = 0

        for i in range(n):
            h = heights[i]
            start = i
            while st and h < st[-1][1]:
                start = st[-1][0]
                area = st[-1][1] * (i - st[-1][0])
                res = max(res, area)
                st.pop()
            
            st.append((start, h))
        
        while st:
            area = st[-1][1] * (n - st[-1][0])
            res = max(res, area)
            st.pop()
        
        return res