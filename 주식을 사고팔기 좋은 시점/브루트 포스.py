from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i,price in enumerate(prices) :
            for j in range(i,len(prices)) :
                profit = max(prices[j]- price ,profit)
        
        return profit