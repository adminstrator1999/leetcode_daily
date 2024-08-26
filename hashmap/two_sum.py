from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, val in enumerate(nums):
            if target - val in hash_map:
                return [hash_map[target - val], i]
            hash_map[val] = i


nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))
