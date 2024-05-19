# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sum = self.generate_int(l1) + self.generate_int(l2)
        
        if sum == 0:
            return ListNode(0, None)
            
        head = ListNode()
        cur = head
        
        while sum:
            new_node = ListNode(sum % 10, None)
            cur.next = new_node
            cur = cur.next
            sum = sum // 10
        
        return head.next
        
        
        
        
    def generate_int(self, ll):
        i = 0
        cur = ll
        ans = 0
        while cur != None:
            ans += cur.val * pow(10, i)
            cur = cur.next
            i += 1

        return int(ans)