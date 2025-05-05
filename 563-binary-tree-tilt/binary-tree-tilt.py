# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = []
    def findTilt(self, root: Optional[TreeNode]) -> int:
        ans = []

        self.recurse(root, ans)

        return sum(ans)
        
    def recurse(self, root, ans):
        if not root:
            return 0

        left = self.recurse(root.left, ans)
        right = self.recurse(root.right, ans)

        ans.append(abs(left - right))

        return root.val + left + right