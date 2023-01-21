# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sums_1=0
        sums_2=0
        counter = 0
        while(l1 != None):
            sums_1 += l1.val*10**counter
            l1 = l1.next
            counter+=1
        counter = 0
        while(l2 != None):
            sums_2 += l2.val*10**counter
            l2 = l2.next
            counter+=1
        to_list = sums_1 + sums_2
        to_list = [int(i) for i in str(to_list) ] [::-1]
        ans = ListNode(to_list[0])
        pointer = ans
        for i in range(1,len(to_list)):
            new_node = ListNode(to_list[i])
            ans.next=new_node
            ans = new_node
        return pointer