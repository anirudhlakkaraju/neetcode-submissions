class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax, rmax = [0] * n, [0] * n

        for i in range(1, n):
            lmax[i] = max(lmax[i-1], height[i-1])
        
        for i in range(n-2, -1, -1):
            rmax[i] = max(rmax[i+1], height[i+1])
        
        res = 0
        for i in range(n):
            res += max(0, min(lmax[i], rmax[i]) - height[i])
        
        return res


