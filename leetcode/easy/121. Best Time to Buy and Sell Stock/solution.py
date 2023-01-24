from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_v = 1234567890
        max_profit = -1
        for p in prices:
            if p < min_v:
                min_v = p
            if p - min_v > max_profit:
                max_profit = p - min_v
        return max_profit
