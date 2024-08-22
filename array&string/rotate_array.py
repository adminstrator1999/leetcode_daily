from typing import List


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        # reverse solution

        # create helper reverse function
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        k %= len(nums)
        n = len(nums) - 1
        reverse(0, n - k)
        reverse(n - k + 1, n)
        reverse(0, n)

    def rotateEasy(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        break_point = (len(nums) - k) % len(nums)
        nums[:] = nums[break_point:] + nums[:break_point]


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
solution = Solution()
solution.rotate(nums, k)
print(nums)
