from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        found = False
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ' and count:
                found = True
            elif s[i] != ' ':
                count += 1
            if found: return count
        return count

    def lengthOfLastWordEasy(self, s: str) -> int:
        return len(s.strip(' ').split(' ')[-1])


# s = "   fly me   to   the moon  "
s = 'k'
solution = Solution()
print(solution.lengthOfLastWord(s))
