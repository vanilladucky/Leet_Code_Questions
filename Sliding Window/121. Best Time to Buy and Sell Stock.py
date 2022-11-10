class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 
        buy_price = 10**4+1
        
        for price in prices:
            buy_price = min(price, buy_price)
            res = max(res, price-buy_price)
            
        return res
