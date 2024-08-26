from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        start = 0

        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                if start == i - 1:
                    ans.append(str(nums[start]))
                else:
                    ans.append(f'{nums[start]}->{nums[i - 1]}')
                start = i

        return ans


    def summaryRangesBrutality(self, nums: List[int]) -> List[str]:
        if not nums: return []
        ans = []
        start = 0
        end = 0
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1:
                end = i + 1
            else:
                if start == end:
                    ans.append(str(nums[start]))
                else:
                    ans.append(f'{nums[start]}->{nums[end]}')
                start = end = i + 1
        if start == end:
            ans.append(str(nums[start]))
        else:
            ans.append(f'{nums[start]}->{nums[end]}')
        return ans


nums = [0, 1, 2, 4, 5, 7]
solution = Solution()
print(solution.summaryRanges(nums))
