class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = 0
        for pile in piles:
            mx = max(mx, pile)
             
        def hours(rate):
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/rate)
            return hrs

        lo, hi = 1, mx
        while lo < hi:
            mid = lo + (hi-lo)//2

            if hours(mid) <= h:
                hi = mid
            else:
                lo = mid + 1
            
        return hi