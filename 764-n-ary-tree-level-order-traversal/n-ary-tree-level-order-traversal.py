"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []
        queue, ans = [], []
        queue.append(root)
        
        while len(queue) != 0:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.children:
                    for i in range(len(node.children)):
                        queue.append(node.children[i])
                
            ans.append(level)
            
        return ans