# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, None)
        ans = head
        if list1 == None and list2 == None:
            return None
        
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                ans.next = list1
                ans = ans.next
                list1 = list1.next
            else:
                ans.next = list2
                ans = ans.next
                list2 = list2.next
                
        while list1 != None:
            ans.next = list1
            ans = ans.next
            list1 = list1.next
        while list2 != None:
            ans.next = list2
            ans = ans.next
            list2 = list2.next
            
        return head.next