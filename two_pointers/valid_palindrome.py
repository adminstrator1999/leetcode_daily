from typing import List


class Solution:

    def isPalindrome(self, s: str) -> bool:
        normalized = "".join(filter(str.isalnum, s.lower()))
        return normalized == normalized[::-1]

    def isPalindrome1(self, s: str) -> bool:
        normalized = ''
        for i in s:
            if i.isalnum():
                normalized += i.lower()
        l, r = 0, len(normalized) - 1
        while l < r:
            if normalized[l] != normalized[r]:
                return False
            l += 1
            r -= 1
        return True

    def isPalindromeEasy(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True


s = "race a car"
solution = Solution()
print(solution.isPalindrome(s))
