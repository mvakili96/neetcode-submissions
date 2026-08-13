class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = prices[0]
        for i in range(1,len(prices)):
            if prices[i] - buy_price > profit:
                profit = prices[i] - buy_price
            
            if prices[i] < buy_price:
                buy_price = prices[i]
        
        return profit

            


        