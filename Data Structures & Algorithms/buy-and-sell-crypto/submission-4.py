class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        max_profit = 0
        for item in prices[1:]:
            if item < min_so_far:
                min_so_far = item
            
            elif item > min_so_far:
                profit = item - min_so_far
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit










            


        