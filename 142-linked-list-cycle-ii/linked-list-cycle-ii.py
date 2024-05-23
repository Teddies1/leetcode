# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        node = self.hasCycle(head)
        if node != None:
            slow = node
            slow2 = head
            while slow != slow2:
                slow = slow.next
                slow2 = slow2.next
            return slow
        else:    
            return None
        
    def hasCycle(self, head):
        if head == None:
            return None
        
        slow = head
        fast = head
        
        while slow != None and fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:    
                return slow
            
        return None