from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        start = 0
        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                if i - 1 == start:
                    ans.append(str(nums[start]))
                else:
                    ans.append(f'{nums[start]}->{nums[i-1]}')
                start = i
        return ans


nums = [0, 1, 2, 4, 5, 7]
solution = Solution()
print(solution.summaryRanges(nums))