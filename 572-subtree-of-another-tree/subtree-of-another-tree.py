# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ans = False
        if root == None or subRoot == None:
            return False
        
        if root.val == subRoot.val:
            ans = self.sameTree(root, subRoot)
            
        if ans == True:
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    
    def sameTree(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None or p.val != q.val:
            return False
        
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        