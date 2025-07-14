# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        curr_head = self.reverse_ll(head)
        ans = 0
        iterator = 0
        
        while curr_head:
            value = curr_head.val * (2**iterator)
            ans += value
            iterator += 1
            curr_head = curr_head.next

        return ans

    def reverse_ll(self, head):
        curr = head
        prev = None
        next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev