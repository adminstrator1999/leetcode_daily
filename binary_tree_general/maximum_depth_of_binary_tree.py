from collections import deque
from typing import Optional
from binary_tree_general import TreeNode, tree


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bfs
        if not root: return 0
        q = deque()
        q.append((root, 1))
        ans = 1
        while q:
            node, level = q.popleft()
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
            ans = max(ans, level)
        return ans

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs
        if not root: return 0
        ans = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return ans

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # stack
        if not root: return 0
        stack = [(root, 1)]
        res = 1
        while stack:
            node, level = stack.pop()
            res = max(level, res)
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
        return res



solution = Solution()
print(solution.maxDepth(tree))

