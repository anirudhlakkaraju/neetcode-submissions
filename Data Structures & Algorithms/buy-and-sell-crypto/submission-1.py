class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        cheapest = prices[0]
        for i in range(1, len(prices), 1):
            res = max(res, prices[i]-cheapest)
            cheapest = min(cheapest, prices[i])
            
        return res