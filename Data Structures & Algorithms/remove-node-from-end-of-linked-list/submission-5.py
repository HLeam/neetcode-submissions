# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        l = 0

        while curr:
            l += 1
            curr = curr.next
        
        removeIndex = l - n
        curr = head
        if removeIndex == 0:
            return curr.next

        i = 0
        while i < l:
            
            if i  == removeIndex -1:
                curr.next = curr.next.next
                break
            curr = curr.next
            i += 1 

        return head

        
        