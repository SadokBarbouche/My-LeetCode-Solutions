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
        if not head or not head.next:
            return
        
        temp = head
        elements = []
        while temp:
            elements.append(temp.val)
            temp = temp.next
        n = len(elements)
        i, j = 0, n - 1
        temp_head = head
        while i < j:
            temp_head.val = elements[i]
            temp_head = temp_head.next
            temp_head.val = elements[j]
            temp_head = temp_head.next
            i += 1
            j -= 1
        if i == j:
            temp_head.val = elements[i]
