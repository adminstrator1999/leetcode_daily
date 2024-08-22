from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0
        last = None
        for n in nums:
            if n == last: continue
            last = n
            nums[cur] = n
            cur += 1
        return cur

    # def removeDuplicates(self, nums: List[int]) -> int:
    #     p1 = 0
    #     for i in range(1, len(nums)):
    #         if nums[p1] == nums[i]:
    #             nums[i] = '_'
    #         else:
    #             p1 += 1
    #             if nums[p1] == '_':
    #                 nums[p1] = nums[i]
    #                 nums[i] = '_'
    #     return p1 + 1


# nums = [1]
nums = [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
solution = Solution()
print(solution.removeDuplicates(nums))
print(nums)
