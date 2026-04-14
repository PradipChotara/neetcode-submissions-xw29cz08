# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def pre(root, low, high):
            if not root:
                return True
            if low < root.val < high:
                return pre(root.left, low, root.val) and pre(root.right, root.val, high)
            else:
                return False

        
        return pre(root, float('-inf'), float('inf'))
        