# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        def mid(node):
            slow ,fast =node,node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def mergeList(l1,l2):
            if not l1:
                return l2
            if not l2 :
                return l1
            if l1.val < l2.val:
                l1.next = mergeList(l1.next,l2)
                return l1
            else:
                l2.next = mergeList(l2.next,l1)
                return l2
        

        left = head
        right = mid(head)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)
        return mergeList(left,right)
