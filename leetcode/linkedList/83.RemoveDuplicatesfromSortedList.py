def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head #1
        while curr and curr.next: 
            if curr.val == curr.next.val: #1==1
                temp =curr.next.next
                curr.next = temp
                # curr.next = curr.next.next
            else:
                curr = curr.next
        return head