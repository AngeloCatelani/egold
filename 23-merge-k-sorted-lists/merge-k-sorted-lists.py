# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists( l1, l2):
            if not l2:
                return l1
            if not l1:
                return l2
            if l1.val < l2.val:
                l1.next = mergeTwoLists(l1.next,l2)
                return l1
            else:
                l2.next = mergeTwoLists(l1,l2.next)
                return l2
        if not lists:
            return None
        while(len(lists))>1:

            mergeList = []
            
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergeList.append(mergeTwoLists(l1,l2))
            lists = mergeList
        return lists[0]

                
                