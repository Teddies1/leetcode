# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        slow, fast = head, head
        while fast != None and fast.next != None:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
            
        if fast != None:
            slow = slow.next
            
        while slow != None:
            if len(stack) != 0 and slow.val != stack.pop():
                return False
            slow = slow.next        
        
        return True