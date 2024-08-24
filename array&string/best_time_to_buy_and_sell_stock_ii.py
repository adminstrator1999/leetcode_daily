from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        start = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > start:
                profit += prices[i] - start
            start = prices[i]
        return profit


prices = [7, 1, 5, 3, 4, 6]
solution = Solution()
print(solution.maxProfit(prices))

