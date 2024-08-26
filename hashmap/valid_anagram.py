from typing import List
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


s = "anagram"
t = "nagaram"
solution = Solution()
print(solution.isAnagram(s, t))
