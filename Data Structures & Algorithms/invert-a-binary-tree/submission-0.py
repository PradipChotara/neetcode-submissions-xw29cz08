# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # base case
        if not root:
            return None

        # convert left and right child first
        li = self.invertTree(root.left)
        ri = self.invertTree(root.right)

        #now swap both childs
        root.left = ri
        root.right = li

        return root
