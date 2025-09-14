# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None:
            return None

        n = len(lists)
        if n == 0:
            return None
        
        heap = []
        dummy = ListNode(None, None)
        ans = dummy
        for i in range(n):
            head = lists[i]
            if head:
                heap.append((head.val, i))
        
        heapq.heapify(heap)
        while heap:
            val, ll_index = heapq.heappop(heap)

            curr = lists[ll_index]
            lists[ll_index] = lists[ll_index].next

            dummy.next = curr
            curr.next = None
            dummy = dummy.next

            if lists[ll_index] != None:
                heapq.heappush(heap, (lists[ll_index].val, ll_index))

        return ans.next

        