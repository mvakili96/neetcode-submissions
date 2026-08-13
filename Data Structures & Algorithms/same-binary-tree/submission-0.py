# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        
        if not p or not q:
            return False

        C1 = p.val == q.val
        C2 = self.isSameTree(p.left,q.left)
        C3 = self.isSameTree(p.right,q.right)

        return C1 and C2 and C3
        








        # C2 = p.right and q.right
        # C3 = p.left and p.left
        # C = C1 and C2 and C3