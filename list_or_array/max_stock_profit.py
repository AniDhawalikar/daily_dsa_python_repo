# find out the max profit from the  data given in the array.
# in which every number is showcase the price of the stock on that day.

def find_max_profit(arr):
    max_profit = 0
    min_price = float("inf")
    n = len(arr)
    for i in range(0,n):
        min_price = min(arr[i], min_price)
        max_profit = max(max_profit, arr[i] - min_price)
    return max_profit

nums = [7,2,1,5,6,4,8]
print(find_max_profit(nums))