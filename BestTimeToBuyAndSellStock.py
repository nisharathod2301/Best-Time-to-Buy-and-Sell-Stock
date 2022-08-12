class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Left pointer: Buy
        #Right pointer: Sell
        #Time Complexity: O(n)
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            #Is this profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
