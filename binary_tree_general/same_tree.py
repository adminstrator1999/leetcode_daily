from collections import deque
from typing import Optional

from binary_tree_general import TreeNode, tree


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # stack
        # check edge cases
        if not p and not q:
            return True
        if not p or not q:
            return False

        stack_p, stack_q = [p], [q]
        while stack_p and stack_q:
            node_p, node_q = stack_p.pop(), stack_q.pop()
            if node_p.val != node_q.val: return False
            if node_p.right or node_q.right:
                # check if node_q.left is equal
                if not node_q.right or not node_p.right:
                    return False
                stack_p.append(node_p.right)
                stack_q.append(node_q.right)

            if node_p.left or node_q.left:
                if not node_q.left or not node_p.left:
                    return False
                stack_p.append(node_p.left)
                stack_q.append(node_q.left)
        return stack_p == stack_q

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # bfs
        if not p and not q:
            return True
        if not p or not q:
            return False
        queue_p, queue_q = deque(), deque()
        queue_p.append(p)
        queue_q.append(q)
        while queue_q and queue_p:
            node_p, node_q = queue_p.popleft(), queue_q.popleft()
            if node_p.val != node_q.val: return False
            if node_p.right or node_q.right:
                if not node_p.right or not node_q.right:
                    return False
                queue_p.append(node_p.right)
                queue_q.append(node_q.right)
            if node_q.left or node_p.left:
                if not node_p.left or not node_q.left:
                    return False
                queue_p.append(node_p.left)
                queue_q.append(node_q.left)
        return queue_q == queue_p

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recursive
        # base cases
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



solution = Solution()
print(solution.isSameTree(tree, tree))
