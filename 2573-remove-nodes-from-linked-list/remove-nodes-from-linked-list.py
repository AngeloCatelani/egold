# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            while stack and stack[-1] < head.val:
                stack.pop()
            else:
                stack.append(head.val)
            head = head.next
        dummy = ListNode(0)
        curr = dummy
        for n in stack:
            curr.next = ListNode(n)
            curr =curr.next
        return dummy.next
            