# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        ans = 0
        self.buildHeap(root, heap)
        print(heap)
        return heap[k-1]
    
    def buildHeap(self, root, heap):
        if root:
            # First recur on left child
            self.buildHeap(root.left, heap)

            # Then print the data of node
            heap.append(root.val)

            # Now recur on right child
            self.buildHeap(root.right, heap)
    
        
        