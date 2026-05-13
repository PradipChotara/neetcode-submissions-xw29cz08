# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_val):
            if not node:
                return 0
            
            count = 0
            left = 0
            right = 0
            if node.val >= max_val:
                count += 1

            max_val = max(max_val, node.val)
            
            if node.left:
                left = dfs(node.left, max_val)
            if node.right:
                right = dfs(node.right, max_val)

            count = count + left + right

            return count
        
        return dfs(root, root.val)