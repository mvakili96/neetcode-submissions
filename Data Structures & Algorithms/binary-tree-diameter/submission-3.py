# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter_ini = 0
        def maxDepth(root):
            if not root:
                return 0

            nonlocal diameter_ini

            depth_left = maxDepth(root.left)
            depth_right = maxDepth(root.right)
            
            diameter_ini = max(diameter_ini,depth_left+depth_right)

            return max(depth_left,depth_right) + 1
     
        maxDepth(root)

        return diameter_ini

        