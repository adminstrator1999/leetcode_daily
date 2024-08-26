from typing import List


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')

        # edge case
        if len(s) != len(pattern):
            return False

        pattern_hm, s_hm = {}, {}
        for i in range(len(pattern)):
            if pattern[i] in pattern_hm and pattern_hm[pattern[i]] != s[i]:
                return False
            if s[i] in s_hm and s_hm[s[i]] != pattern[i]:
                return False
            pattern_hm[pattern[i]] = s[i]
            s_hm[s[i]] = pattern[i]
        return True

    def wordPatternEasy(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(s) != len(pattern):
            return False
        hash_map = {}
        for i in range(len(pattern)):
            if (pattern[i] in hash_map and hash_map[pattern[i]] != s[i]) or \
               (pattern[i] not in hash_map and s[i] in hash_map.values()):
                return False
            hash_map[pattern[i]] = s[i]
        return True

pattern = "abba"
s = "dog cat cat dog"
solution = Solution()
print(solution.wordPattern(pattern, s))
