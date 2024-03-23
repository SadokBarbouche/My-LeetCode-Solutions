# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        current = head
        while current and current.next:
            gcd = math.gcd(current.val, current.next.val)
            node_insert = ListNode(val=gcd)
            node_insert.next = current.next
            current.next = node_insert
            current = current.next.next
        return head
