# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def solve(node):
            if not node:
                return 0
            l = solve(node.left)
            r = solve(node.right)

            if l == -1 or r == -1:
                return -1

            if l-r >= 2 or r-l >= 2:
                return -1
            else:
                return max(l,r) + 1

        return solve(root) != -1
        