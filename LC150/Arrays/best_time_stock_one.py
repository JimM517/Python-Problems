# 121 best time to buy and sell stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 0:
            return 0
        
        
        first = prices[0]
        maxProfit = 0
        
        for price in prices:
            if price < first:
                first = price
            
            else:
                current_profit = price - first
                
                if current_profit > maxProfit:
                    maxProfit = current_profit
        
        return maxProfit
    

prices = [7,1,5,3,6,4]
    
sol = Solution()

print(sol.maxProfit(prices))

        