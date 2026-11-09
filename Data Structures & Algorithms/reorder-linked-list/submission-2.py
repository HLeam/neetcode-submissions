# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # we need to get the behind half of the linked list 
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the linked list
        prev = None
        # 6 -> 8 -> none
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt


        # now we need to merge the reverse half with the beginning half 
        curr = head
        
        while prev.next:
            temp1 = curr.next 
            temp2 = prev.next 

            curr.next = prev 
            prev.next = temp1 

            curr = temp1 
            prev = temp2 # 8






            


        