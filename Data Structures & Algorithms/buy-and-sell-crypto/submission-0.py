class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #  O(n) time and O(1) space
        l = 0
        r = l + 1
        maxProfit = 0

        while r < len(prices):
            maxProfit = max(maxProfit, prices[r] - prices[l])
            
            if (prices[l] >= prices[r]):
                l = r

            r += 1

        return maxProfit