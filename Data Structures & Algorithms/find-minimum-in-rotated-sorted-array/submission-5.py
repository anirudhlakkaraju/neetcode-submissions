class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0] < nums[n-1]:
            return nums[0]

        lo, hi = 0, n-1
        while lo < hi:
            mid = lo + (hi-lo)//2

            if nums[0] <= nums[mid]:
                lo = mid + 1
            else:
                hi = mid
        
        return nums[hi]