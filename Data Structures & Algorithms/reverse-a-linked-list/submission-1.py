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

        end = len(store) - 1

        for i in range(len(store) - 1):
            store[end].next = store[end - 1]
            end -= 1

        store[0].next = None

        return store[-1]
