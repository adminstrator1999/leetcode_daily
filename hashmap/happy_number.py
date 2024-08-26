from typing import List


class Solution:
    def addSquaredNumbers(self, n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n //= 10
        return output

    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.addSquaredNumbers(n)

        while slow != fast:
            fast = self.addSquaredNumbers(fast)
            fast = self.addSquaredNumbers(fast)
            slow = self.addSquaredNumbers(slow)
        return True if fast == 1 else False

    def isHappyEasy(self, n: int) -> bool:
        hash_set = set()
        tmp = self.addSquaredNumbers(n)
        while tmp not in hash_set:
            if tmp == 1:
                return True
            hash_set.add(tmp)
            tmp = self.addSquaredNumbers(tmp)
        return False





n = 3
solution = Solution()
print(solution.isHappy(n))
