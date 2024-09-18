from typing import Optional

from binary_tree_general import TreeNode, tree


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def helper(root, target):
            if target == 0 and not root.left and not root.right:
                return True
            if root.left:
                if helper(root.left, target - root.left.val):
                    return True
            if root.right:
                if helper(root.right, target - root.right.val):
                    return True
            return False
        return helper(root, targetSum - root.val)

solution = Solution()
print(solution.hasPathSum(root=tree, targetSum=17))
