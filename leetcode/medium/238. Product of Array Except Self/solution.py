from typing import *


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        num_of_zero = 0
        for n in nums:
            if n == 0:
                num_of_zero += 1

        if num_of_zero > 1:
            return list(0 for _ in range(len(nums)))
        if num_of_zero > 0:
            for n in nums:
                if n == 0:
                    continue
                product *= n
            return list(product if n == 0 else 0 for n in nums)

        for n in nums:
            product *= n

        return list(product // n for n in nums)
