# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node that points to the head of the list
        dummy = ListNode(0)
        dummy.next = head
        # Initialize current pointer to the dummy node
        curr = dummy
        
        # Traverse the list until the end
        while curr.next:
            # If the next node's value matches the target value, skip it
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                # Otherwise, move the current pointer to the next node
                curr = curr.next
        
        # Return the new head of the list, which is dummy.next
        return dummy.next
