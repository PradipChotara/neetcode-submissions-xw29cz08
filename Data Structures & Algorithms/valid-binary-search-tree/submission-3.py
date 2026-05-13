# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ls = []

        def inorder(node):
            if not node:
                return 0
            inorder(node.left)
            ls.append(node.val)
            inorder(node.right)
        
        inorder(root)
        for i in range(len(ls)-1):
            if ls[i] >= ls[i+1]:
                return False
        return True