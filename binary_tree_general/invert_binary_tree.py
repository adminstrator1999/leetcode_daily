from typing import Optional

from binary_tree_general import TreeNode, tree


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

solution = Solution()
print(solution.invertTree(tree))
