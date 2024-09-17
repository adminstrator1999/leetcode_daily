from collections import deque
from inspect import stack


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
                    1
               /         \
              2            3
           /     \       /    \
         4        5     6      7
       /   \     /
     8      9   10
"""
def create_tree(tree: [int]) -> TreeNode:
    q = deque()
    head = TreeNode(1)
    q.append(head)
    i = 1
    while q and i < len(tree):
        node = q.popleft()
        node.left = TreeNode(tree[i])
        q.append(node.left)
        i += 1
        if i < len(tree):
            node.right = TreeNode(tree[i])
            q.append(node.right)
            i += 1
    return head
tree = create_tree(arr)

def print_tree(root, ans = []):
    # preorder recursive
    if not root: return
    print(root.val)
    ans.append(root.val)
    print_tree(root.left)
    print_tree(root.right)
    print(ans)
# [1, 2, 4, 8, 9, 5, 10, 3, 6, 7]

def print_tree_iterative(root):
    if not root: return
    ans = []
    stack = [root]
    while stack:
        node = stack.pop()
        ans.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return ans
print(print_tree_iterative(tree))