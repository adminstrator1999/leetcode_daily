from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        # this solution is removes items from the end of the list
        slow = len(nums) - 1
        count = 0
        for fast in range(len(nums) - 1, -1, -1):
            if nums[fast] == val:
                nums[fast] = nums[slow]
                nums[slow] = -1
                slow -= 1
                count += 1
        return len(nums) - count

    def removeElementMagic(self, nums: List[int], val: int) -> int:
        # python magic but inefficient
        while val in nums:
            nums.remove(val)

        return len(nums)

    def removeElementBrute(self, nums: List[int], val: int) -> int:
        start, end = 0, len(nums) - 1
        count = 0
        while start <= end:
            if nums[end] == val:
                nums[end] = '_'
                end -= 1
                count += 1
            elif nums[start] == val:
                nums[start] = nums[end]
                nums[end] = '_'
                end -= 1
                start += 1
                count += 1
            else:
                start += 1
        return len(nums) - count


# nums = [0, 1, 2, 2, 3, 0, 4, 2]
# val = 2
nums = [3, 2, 2, 3]
val = 3
solution = Solution()
print(solution.removeElement(nums, val))
print(nums)
