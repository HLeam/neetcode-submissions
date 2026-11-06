# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode()
        dummy = new_node

        while list1 and list2:
            val1 = list1.val
            val2 = list2.val

            if val1 > val2:
                dummy.next = list2
                list2 = list2.next
            else:
                dummy.next = list1
                list1 = list1.next

            dummy = dummy.next

        dummy.next = list1 if list1 else list2

        return new_node.next
            




        
        