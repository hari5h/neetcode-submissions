class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, len(prices)
        profit = 0

        for r in range(len(prices)):
            profit = max(profit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r

        
        return profit



'''
buy 
sell
profit > 0 
5

[1,2] --> int

9, 1, 5, 6, 7, 1
l  r
profit-8


l<r && num[l] > num[r]
l = r

r = r+1
9, 1, 5, 6, 7, 1
   l        r
'''

