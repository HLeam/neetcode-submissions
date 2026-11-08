# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # we want to get the middle of the array so we have 

        # reverse the middle to end of the array
        # have a pointer on head then sum them and keep track of the max 
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        # 2 -> 1 -> None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        max_ = 0
        curr = head
        while prev:
            max_ = max(max_, prev.val + curr.val)
            prev = prev.next
            curr = curr.next
        
        return max_