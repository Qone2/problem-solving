from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]
        return profit


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
