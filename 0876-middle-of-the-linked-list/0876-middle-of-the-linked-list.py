# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size_pointer = head
        size = 0

        while size_pointer:
            size += 1
            size_pointer = size_pointer.next

        middle = size // 2

        for _ in range(middle):
            head = head.next

        return head