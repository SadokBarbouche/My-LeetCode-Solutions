# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = head
        length = 0
        
        while first:
            length += 1
            first = first.next
        
        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next
        
        first.next = first.next.next
        
        return dummy.next