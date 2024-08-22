from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        cheapest = prices[0]
        profit = 0
        for num in prices[1:]:
            if num < cheapest:
                cheapest = num
            profit = max(profit, num - cheapest)
        return profit


prices = []
solution = Solution()
print(solution.maxProfit(prices))
