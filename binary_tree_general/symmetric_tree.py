from typing import Optional

from binary_tree_general import TreeNode, tree


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False

        # divide it into two trees and traverse them simultaneously
        stack_left, stack_right = [root.left], [root.right]
        while stack_left and stack_right:
            left_node = stack_left.pop()
            right_node = stack_right.pop()
            if left_node.val != right_node.val:
                return False
            if left_node.right or right_node.left:
                if not left_node.right or not right_node.left:
                    return False
                stack_left.append(left_node.right)
                stack_right.append(right_node.left)
            if left_node.left or right_node.right:
                if not left_node.left or not right_node.right:
                    return False
                stack_left.append(left_node.left)
                stack_right.append(right_node.right)
        return stack_right == stack_left

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def func(right, left):
            if not left and not right:  # step1 case 1
                return True
            if not left or not right:  # step1 case 2
                return False

            if right.val == left.val:  # step2
                outpair = func(left.left, right.right)
                inpair = func(left.right, right.left)
                return outpair and inpair
            else:
                return False



solution = Solution()
print(solution.isSymmetric(tree))
