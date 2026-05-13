# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def solve(node, left, right):
            if not node:
                return True
            
            if not (left < node.val < right):
                return False
            
            left_sub = solve(node.left, left, node.val)
            if not left_sub:
                return False
            
            right_sub = solve(node.right, node.val, right)
            if not right_sub:
                return False

            return True

        left = float('-inf')
        right = float('inf')    
        return solve(root, left, right)