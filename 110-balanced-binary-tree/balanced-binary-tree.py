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
        
        left = self.findHeight(root.left)
        right = self.findHeight(root.right)
    
        if abs(left - right) > 1:
            return False
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
        
        return True
    
    
    def findHeight(self, root):
        if not root:
            return 0
        left = 1 + self.findHeight(root.left)
        right = 1 + self.findHeight(root.right)
        
        return max(left, right)