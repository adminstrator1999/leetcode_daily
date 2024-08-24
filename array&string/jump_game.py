from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # we can solve this greedy
        # in each step we can reduce our curr jump ability by one
        # but if in our current position has bigger jump ability we update
        cur = 0
        for num in nums:
            if cur < 0: return False
            if num > cur: cur = num
            cur -= 1
        return True

    def canJump1(self, nums: List[int]) -> bool:
        length = len(nums) - 1
        before = length - 1
        while length:
            if before < 0:
                return False
            if length <= before + nums[before]:
                length = before
            before -= 1
        return length == 0


nums = [2, 3, 1, 1, 0]
solution = Solution()
print(solution.canJump(nums))
