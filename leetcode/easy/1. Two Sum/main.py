from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] + nums[i] == target:
                    answer.append(i)
                    answer.append(j)
                    return answer
