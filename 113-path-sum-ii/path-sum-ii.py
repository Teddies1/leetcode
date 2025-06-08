# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        self.recurse(root, targetSum, [], ans)

        return ans

    def recurse(self, node, targetSum, path, ans):
        if not node:
            return
        
        if node.left == None and node.right == None:
            currSum = sum(path) + node.val
            path.append(node.val)
            if currSum == targetSum:
                ans.append(path[:])
                path.pop()
                return
            else:
                path.pop()
                return

        path.append(node.val)
        self.recurse(node.left, targetSum, path, ans)
        self.recurse(node.right, targetSum, path, ans)
        path.pop()
