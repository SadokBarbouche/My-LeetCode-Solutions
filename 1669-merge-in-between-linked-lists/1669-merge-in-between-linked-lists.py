class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        if a == 0:
            return list2
        
        index = 0
        prev_node = list1
        while index < a - 1:
            prev_node = prev_node.next
            index += 1

        index = 0
        next_node = prev_node
        while index < b - a + 1:
            next_node = next_node.next
            index += 1

        prev_node.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = next_node.next

        return list1
