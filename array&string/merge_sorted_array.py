from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l, r, b = m-1, n-1, n+m-1
        while b >= 0:
            # if nums2 is checked we can stop iteration
            if r < 0:
                break
            if l < 0 or nums1[l] < nums2[r]:
                nums1[b] = nums2[r]
                r -= 1
            else:
                nums1[b] = nums1[l]
                l -= 1
            b -= 1


# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3
nums1 = [0]
m = 0
nums2 = [1]
n = 1
solution = Solution()
solution.merge(nums1, m, nums2, n)
print(nums1)
