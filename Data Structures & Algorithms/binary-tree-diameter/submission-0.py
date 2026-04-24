# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.max_dia = 0

        def solve(root):
            if not root:
                return 0
            
            l = solve(root.left)
            r = solve(root.right)

            self.max_dia = max(self.max_dia, l+r)

            return max(l,r) + 1

        solve(root)
        return self.max_dia