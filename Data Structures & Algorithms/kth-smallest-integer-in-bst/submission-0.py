# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.count = 0

        def inorder(root, k):

            if not root:
                return

            left = inorder(root.left, k)
            if left:
                return left

            self.count += 1
            if self.count == k:
                return root.val

            right = inorder(root.right, k)
            if right:
                return right

        return inorder(root, k)