# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head : return head
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length+=1
          # Compute the effective number of rotations needed, 
        # as rotating a list by its length results in the same list
        k = k % length
        
        # If no rotation is needed, return the head as it is
        if k == 0:
            return head
        curr = head
        for i in range(length -k -1):
            curr = curr.next
        tmp = curr.next
        curr.next = None
        tail.next = head

        return tmp



        