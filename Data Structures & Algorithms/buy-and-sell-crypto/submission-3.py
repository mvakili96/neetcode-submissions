class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = prices[0]
        profit = 0
        for price in prices[1:]:
            if price <= min_:
                min_ = price

            if price - min_ >= profit:
                profit = price - min_
        
        return profit







            


        