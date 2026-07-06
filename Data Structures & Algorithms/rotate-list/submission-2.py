# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        tail = head
        n = 1

        while tail.next:
            n+=1
            tail = tail.next

        k = k % n
        if k ==0:
            return head

        curr = head
        for _ in range(n-k-1):
            curr = curr.next

        newHead = curr.next
        curr.next = None
        tail.next = head

        return newHead


