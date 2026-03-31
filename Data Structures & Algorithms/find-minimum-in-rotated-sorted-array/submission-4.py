class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n-1

        if nums[0] <= nums[n-1]:
            return nums[0]

        while lo < hi:
            mid = lo + (hi-lo)//2

            if nums[n-1] >= nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        
        return nums[hi]
            