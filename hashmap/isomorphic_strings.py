from typing import List
from collections import Counter


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_hm, t_hm = {}, {}

        for i in range(len(s)):
            if s[i] in s_hm and s_hm[s[i]] != t[i]:
                return False

            if t[i] in t_hm and t_hm[t[i]] != s[i]:
                return False

            s_hm[s[i]] = t[i]
            t_hm[t[i]] = s[i]
        return True
    def isIsomorphicEasy(self, s: str, t: str) -> bool:
        # some difficulty understanding
        hash_map = {}
        for i in range(len(s)):
            if ((s[i] in hash_map and hash_map[s[i]] != t[i]) or
                    (s[i] not in hash_map and t[i] in hash_map.values())):
                return False
            hash_map[s[i]] = t[i]
        return True


s = "b"
t = "b"
solution = Solution()
print(solution.isIsomorphic(s, t))
