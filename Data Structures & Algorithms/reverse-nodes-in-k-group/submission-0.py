# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_node = ListNode(0, head)
        groupPrev = new_node

        while True:
            kth = self.getKthNode(groupPrev, k)
            if not kth:
                break
            nextGroup = kth.next

        # Reverse the LinkedList 
            prev = nextGroup
            curr = groupPrev.next
            while curr != nextGroup:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return new_node.next

    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

            
        