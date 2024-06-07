# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return None
        ans, deque = [], []
        deque.append(root)
        flag = 0
        
        while len(deque) != 0:
            array = []
            for i in range(len(deque)):
                node = deque.pop(0)
                if flag == 0:
                    array.append(node.val)
                else:
                    array.insert(0, node.val)
                print(node.val)
                
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            flag ^= 1
            ans.append(array)
        
        return ans
    
    
    