# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issame(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return (issame(p.left,q.left) and issame(p.right,q.right))
        
        def findroot(root):
            if not root:
                return False
            if root.val == subRoot.val:
                if issame(root,subRoot):
                    return True
            return (findroot(root.left) or findroot(root.right))

        return findroot(root)