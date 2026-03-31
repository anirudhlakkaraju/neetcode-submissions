class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        l, r = 0, 0
        q = collections.deque()
        res = []

        for r in range(n):
            
            # pop the smallest values
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # since q contains indices, if l has advanced
            # ahead of the left most bound of q, then pop
            # Basically shrink the window
            if l > q[0]:
                q.popleft()
            
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
        
        return res
            
