# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = []
        current_node = list1
        while current_node:
            heapq.heappush(merged, current_node.val)
            current_node = current_node.next
        current_node = list2
        while current_node:
            heapq.heappush(merged, current_node.val)
            current_node = current_node.next
        
        dummy = ListNode(-1)
        ans = dummy
        while merged:
            ans.next = ListNode(heapq.heappop(merged))
            ans = ans.next
            
        return dummy.next