# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root == None:
            return None
        ans, queue = [], []
        queue.append(root)
        
        while len(queue) != 0:
            array = []
            for i in range(len(queue)):
                node = queue.pop(0)
                array.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(sum(array) / len(array))
        
        return ans