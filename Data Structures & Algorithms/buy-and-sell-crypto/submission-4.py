class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i] > max_profit:
                max_profit = prices[i+1] - prices[i]
            if prices[i] < prices[i+1]:
                aux = prices[i]
                prices[i] = prices[i+1]
                prices[i+1] = aux
        
        return max_profit

        


        