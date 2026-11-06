# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        store = []
        curr = head
        while curr:
            store.append(curr)
            curr = curr.next

        if not store:
            return None
        
        for i in reversed(range(1, len(store))):
            store[i].next = store[i - 1]

        store[0].next = None

        return store[-1]


        
            