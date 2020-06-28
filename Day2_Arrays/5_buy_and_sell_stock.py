# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.


def maxProfitBrute(arr):
    # O(n^2)

    arr_len = len(arr)
    profit = -1

    for i in range(arr_len-1):
        for j in range(i+1, arr_len):
            diff = arr[j]-arr[i]
            if (profit <= diff):
                profit = diff
                start = i
                end = j

    return start, end, arr[end]-arr[start]


def maxProfit(prices):
    # O(n)
    arr = prices
    arr_len = len(arr)

    if len(arr) < 2:
        return 0

    elif len(arr) == 2:
        return arr[1]-arr[0] if arr[1] > arr[0] else 0

    mini = arr[0]
    profit = arr[1]-arr[0]
    for idx, item in enumerate(arr):
        mini = min(mini, item)
        profit = max(profit, item-mini)
    return profit


arr = [5, 5]
# arr_len = len(arr)
# start, end, profit = bestBuy(arr, arr_len)
# print(f'start = {start}\nend = {end}\nProfit = {profit}')

profit = maxProfit(arr)
print(f'\nProfit = {profit}')
