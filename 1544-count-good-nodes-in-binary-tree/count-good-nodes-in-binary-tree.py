# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def goodNodes(self, root: TreeNode) -> int:
        '''
        inorder traversal
        keep track of current max of the path, starting from root.val
        if the node is >= current max, +1 to good nodes
        '''
        self.recurse(root, root.val, self.ans)
        
        return self.ans


    def recurse(self, node, currmax, ans):
        if node:
            currmax = max(currmax, node.val)
            self.recurse(node.left, currmax, self.ans)
            if node.val >= currmax:
                self.ans += 1
            self.recurse(node.right, currmax, self.ans)