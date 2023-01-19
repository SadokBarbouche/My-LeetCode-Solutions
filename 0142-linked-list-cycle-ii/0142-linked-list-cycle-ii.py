# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # using Floyd Cycle Algorithm
        if head == None :
            return None
        fast = head
        slow = head
        while ( fast != None and slow != None and fast.next != None ):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                while slow != fast :
                    slow = slow.next
                    fast = fast.next
                return slow
        return None