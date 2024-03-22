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
        
        n = len(values)
        
        for i in range(n // 2):
            if values[i] != values[n- 1 - i]:
                return False
            
        return True