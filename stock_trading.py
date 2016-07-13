"""
Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

"""
# Basically the stocks are in order. It says 'yesterday', so if stock closing time is midnght,  12*60+30 is the largest possible index
# I need to find the greatest (positive) distant between points. 

# I wonder if there is a way to do this in O(n) time, by keeping track of the current best deal.

def get_max_profit(prices):
    
    if len(prices) < 2:
        raise error("We need more prices!")
    
    current_lowest = 0
    possible_lowest = 0
    current_highest = 1
    
    for p in range(len(prices)):
        if prices[p] < prices[current_lowest] and prices[p] < prices[possible_lowest]:
            possible_lowest = p
        if prices[p] - prices[possible_lowest] > prices[current_highest] - prices[current_lowest] and p - possible_lowest > 1: 
            current_highest = p
            current_lowest = possible_lowest
            
    return prices[current_highest] - prices[current_lowest]        
            

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

print get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)