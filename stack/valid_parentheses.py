class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for b in s:
            if stack:
                if b in pairs and stack[-1] == pairs[b]:
                    stack.pop()
                    continue
            else:
                if b in pairs:
                    return False
            stack.append(b)
        return len(stack) == 0

    def isValidEasy(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}
        for item in s:
            if item in pairs:
                if stack and stack[-1] == pairs[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
        return not stack



s = "(])"
solution = Solution()
print(solution.isValid(s))