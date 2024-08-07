# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack, arr = [], []
        curr = root
        while curr != None or len(stack) != 0:
            while curr != None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            arr.append(curr.val)
            curr = curr.right
        
        for i in range(len(arr)-1):
            if arr[i] >= arr[i+1]:
                return False
        
        
        return True