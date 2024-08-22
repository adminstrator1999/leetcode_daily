from typing import List
from collections import Counter


class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Majority Voting Algorithm
        # the point is if one number appears majority times (n // 2 + 1)
        # this means that even if we subtract all other numbers count result would be more than 0
        count = 0
        candidate = -1
        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
                count += 1
            else:
                if nums[i] == candidate:
                    count += 1
                else:
                    count -= 1
        return candidate


    def majorityElementEasy(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for k, v in counter.items():
            if v > len(nums) // 2:
                return k


nums = [3, 2, 3]
nums = [2, 1, 2, 3, 3, 3, 3]
solution = Solution()
print(solution.majorityElement(nums))
