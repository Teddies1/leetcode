# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        
        cur = head
        while cur != None:
            nums.append(cur.val)
            cur = cur.next
        
        nums.sort()        
        ans = ListNode()
        new = ans
        
        for num in nums:
            num_node = ListNode(num, None)
            new.next = num_node
            new = new.next
            
        return ans.next