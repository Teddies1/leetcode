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

        self.recurse(root, targetSum, 0, [], ans)

        return ans

    def recurse(self, node, targetSum, currSum, path, ans):
        if not node:
            return
        
        if node.left == None and node.right == None:
            currSum += node.val
            path.append(node.val)
            if currSum == targetSum:
                print(path, currSum)
                ans.append(path[:])
                path.pop()
                return
            else:
                path.pop()
                return

        path.append(node.val)
        self.recurse(node.left, targetSum, currSum + node.val, path, ans)
        self.recurse(node.right, targetSum, currSum + node.val, path, ans)
        path.pop()
