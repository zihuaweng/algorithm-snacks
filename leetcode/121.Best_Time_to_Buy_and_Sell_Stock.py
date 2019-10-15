# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 设置三个指针往前移动
# buy要在sell的前面，指针p往前走，只要有比sell大，更新sell，如果比buy小，初始化sell，buy为p

class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        profit = 0
        buy = 0
        sell = 0
        p = 0
        while p < len(prices):
            if prices[p] > prices[sell]:
                sell = p
            if prices[p] < prices[buy]:
                buy = p
                sell = p

            profit = max(prices[sell] - prices[buy], profit)
            p += 1

        return profit


# 比较简单的写法：
# 记录买时间，后面遇到较大的就计算profit
# 如果遇到更小的buy就替换
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        buy = prices[0]
        for i in prices:
            if i < buy:
                buy = i
            if i > buy:
                profit = max(profit, i - buy)
        return profit

