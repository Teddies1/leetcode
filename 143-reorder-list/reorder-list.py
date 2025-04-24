# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        '''
        idea is to find the middle of the linked list
        reverse the nodes after the middle
        interweave the 2 lists
        
        1->2->3->4
        middle is 2
        1->2 + 3->4
        after reverse:
        1->2 + 4->3
        interweave:
        1->4->2->3


        1->2->3->4->5
        middle is 3, nodes after 3 is 4->5
        after reverse:
        1->2->3 + 5->4
        interweave
        1->5->2->4->3
        '''
        # find middle
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # reverse nodes after middle
        second_curr = slow.next
        slow.next = None
        prev = None
        while second_curr:
            next_node = second_curr.next
            second_curr.next = prev
            prev = second_curr
            second_curr = next_node

        # interweave nodes

        curr, second_curr = head, prev

        while curr and second_curr:
            next_curr = curr.next
            next_second_curr = second_curr.next

            curr.next = second_curr
            second_curr.next = next_curr

            curr = next_curr
            second_curr = next_second_curr
        
        return curr

        '''
        1->2->3  
        c  n
        5->4
        s  n
        

        1->5->2->4
        interweave
        1->5->2->4->3
        '''
