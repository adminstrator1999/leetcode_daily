from collections import deque
from typing import Optional

from binary_tree_general import TreeNode, tree


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        count = 0
        while queue:
            temp = queue.popleft()
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            count += 1
        return count


solution = Solution()
print(solution.countNodes(tree))
