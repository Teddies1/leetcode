# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = []
        parent_map = {}
        if not root:
            return False
        depth = 0
        queue.append(root)
        parent_map[root.val] = (None, depth) 

        while queue:
            for i in range(len(queue)):
                curr_node = queue.pop(0)
                if curr_node.left:
                    queue.append(curr_node.left)
                    parent_map[curr_node.left.val] = (curr_node.val, depth+1)
                if curr_node.right:
                    queue.append(curr_node.right)
                    parent_map[curr_node.right.val] = (curr_node.val, depth+1)

            depth += 1
            
        x_parent, x_depth = parent_map[x]
        y_parent, y_depth = parent_map[y]

        if x_parent != y_parent and x_depth == y_depth:
            return True

        return False