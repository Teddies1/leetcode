# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = []
        curr_level = 0
        if not root:
            return False
        
        queue.append(root)

        while queue:
            level = []
            parity = curr_level % 2
            for _ in range(len(queue)):
                curr_node = queue.pop(0)
                level.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            for value in level:
                if value % 2 != (1-parity):
                    return False
            
            for i in range(1, len(level)):
                if parity == 0:
                    if level[i-1] >= level[i]:
                        return False
                else:
                    if level[i-1] <= level[i]:
                        return False

            curr_level += 1
            
        return True
            