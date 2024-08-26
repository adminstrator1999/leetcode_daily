from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0] and haystack[i: i+len(needle)] == needle:
                return i
        return res


haystack = "i"
needle = "i"
solution = Solution()
print(solution.strStr(haystack, needle))
