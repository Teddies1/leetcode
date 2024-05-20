# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.get_length(head)
        cur = head
        
        if cur.next == None:
            return None
        if length - n == 0:
            return head.next
        
        for i in range(1, length - n):
            cur = cur.next
        if cur.next != None and cur.next.next != None:
            cur.next = cur.next.next
        else: 
            cur.next = None
        
        
        return head
    
    def get_length(self, head):
        cur = head
        ans = 0
        while cur != None:
            ans += 1
            cur = cur.next
            
        return ans