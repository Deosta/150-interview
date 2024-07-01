# 1. Initialize variables buy_price with the first element of the prices array and profit as 0.
# 2. Iterate through the prices starting from the second element.
# 3. Update the buy variable if the current price is lower than the current buying price.
# 4. Update the profit if the difference between the current price and the buying price is greater than the current profit.
# 5. Return the final profit.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #initialize the buy price, set it to the first value in the array
        buy_price = prices[0]
        #initialize the variable we will return
        profit = 0
        #iterate through the prices array
        for i in range(1, len(prices)):
            #find the best 'day' to buy
            if buy_price > prices[i]:
                buy_price = prices[i]
            #find the greatest profit
            if prices[i] - buy_price > profit:
                profit = prices[i] - buy_price
        return profit