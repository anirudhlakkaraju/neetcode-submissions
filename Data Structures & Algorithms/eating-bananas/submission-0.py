class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        
        def hours(rate):
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / rate)
            return hrs
        
        r = 0
        for pile in piles:
            r = max(pile, r)

        lo, hi = 1, r
        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if hours(mid) > h:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return lo 