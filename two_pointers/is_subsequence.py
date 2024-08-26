from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        p = 0
        for i in t:
            if s[p] == i:
                p += 1
            if p == len(s):
                return True
        return False


s = "abc"
t = "ahbgdc"
s = ""
t = ""
solution = Solution()
print(solution.isSubsequence(s, t))
