from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:
        pairs = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000
                 }
        double_pairs = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        i = len(s) - 1
        res = 0
        while i >= 0:
            if s[i-1: i + 1] in double_pairs:
                res += double_pairs[s[i-1: i + 1]]
                i -= 2
            else:
                res += pairs[s[i]]
                i -= 1
        return res


s = "IXIV"
solution = Solution()
print(solution.romanToInt(s))
