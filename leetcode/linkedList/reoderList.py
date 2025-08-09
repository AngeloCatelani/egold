class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
      
        # # using two pointers fast and second
    #     second half
#  [1,2,3,4,5]
#   s   fs   f
        slow,fast = head,head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second=slow.next
        prev = None
        slow.next = None
# reversing
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # merging two halfs
        first ,second = head,prev
         
        while second: #second half is shorter
            tmp1,tmp2 = first.next,second.next 
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
    # work on reorder again