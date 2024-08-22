from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        insert_index = 2
        for i in range(2, len(nums)):
            # unique item is found
            if nums[i-1] != nums[i] or nums[insert_index - 2] != nums[i]:
                nums[insert_index] = nums[i]
                insert_index += 1
        return insert_index

    # def removeDuplicates(self, nums: List[int]) -> int:
    #     p, count = 0, 0
    #     last = None
    #     for num in nums:
    #         if last == num:
    #             count += 1
    #             if count <= 2:
    #                 nums[p] = num
    #                 p += 1
    #             continue
    #         count = 1
    #         last = num
    #         nums[p] = num
    #         p += 1
    #     return p


nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
solution = Solution()
print(solution.removeDuplicates(nums))
print(nums)
