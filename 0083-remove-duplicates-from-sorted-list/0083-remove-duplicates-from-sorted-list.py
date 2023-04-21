# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = set()
        while head != None:
            s.add(head.val)
            head = head.next
        s = sorted(s)
        ans = ListNode()
        current = ans
        for i in s:
            current.next = ListNode(i)
            current = current.next
        return ans.next
            
            