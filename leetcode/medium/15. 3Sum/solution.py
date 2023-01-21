from typing import *


class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     # 중복을 거르기 위해 set으로 함
    #     answer = set()
    #     nums.sort()
    #     # 모든 순열이 아닌 조합에 대하여 시도해본다.
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             for k in range(j + 1, len(nums)):
    #                 if nums[i] + nums[j] + nums[k] == 0:
    #                     answer.add((nums[i], nums[j], nums[k]))
    #     answer_list = []
    #     for a in answer:
    #         answer_list.append([a[0], a[1], a[2]])
    #     return answer_list

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum_num = nums[i] + nums[left] + nums[right]
                if sum_num < 0:
                    left += 1
                elif sum_num > 0:
                    right -= 1
                elif sum_num == 0:
                    answer.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return answer


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
