# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # l1,l2 = headA,headB
        # while l1 != l2:
        #     l1 = l1.next if l1 else headB
        #     l2 = l2.next if l2 else headA
         
        # return l1
        # # time O(n+m)
   
        hashSet = set()
        
        # Traverse the first list and store its nodes in the set
        curr = headA
        while curr:
            hashSet.add(curr)
            curr = curr.next
        
        # Traverse the second list and check if any node is in the set
        curr2 = headB
        while curr2:
            if curr2 in hashSet:
                return curr2
            curr2 = curr2.next
        
        # If no intersection is found, return None
        return None
