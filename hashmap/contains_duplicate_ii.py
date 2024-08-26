from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        for i, num in enumerate(nums):
            if num in hash_map and abs(hash_map[num] - i) <= k:
                return True
            hash_map[num] = i
        return False


nums = [1, 2, 3, 1]
k = 3
solution = Solution()
print(solution.containsNearbyDuplicate(nums, k))
