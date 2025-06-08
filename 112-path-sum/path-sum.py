# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False

        return self.recurse(root, targetSum, 0)
    
    def recurse(self, node, targetSum, val):
        if not node:
            return False

        if node.left == None and node.right == None:
            val += node.val
            if val == targetSum:
                return True

        return self.recurse(node.left, targetSum, val + node.val) or self.recurse(node.right, targetSum, val + node.val)