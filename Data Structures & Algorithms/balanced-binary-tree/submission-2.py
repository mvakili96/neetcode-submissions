# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def checkBalance(root):
            def findHeight(root):
                if not root:
                    return 0
                height_left  = 0
                height_right = 0
                height_left = 1 + findHeight(root.left)
                height_right = 1 + findHeight(root.right)          
                return max(height_left,height_right)        
            if not root:
                return True
            height_left  = findHeight(root.left)
            height_right = findHeight(root.right)
            right_decision = checkBalance(root.right)
            left_decision = checkBalance(root.left)
            return abs(height_left-height_right) <= 1 and right_decision and left_decision     
        return checkBalance(root)
        