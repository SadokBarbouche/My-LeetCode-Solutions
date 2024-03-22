# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        values = []
        
        while head:
            values.append(head.val)
            head = head.next
            
        if values == values[::-1]:
            return True
        
        return False