# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            
            left_height = height(root.left)
            right_height = height(root.right)

            if left_height is False or right_height is False:
                return False

            if abs(left_height - right_height) > 1:
                return False
            
            return 1 + max(left_height, right_height)
            
        if height(root) is False:
            return False
        else:
            return True
        
        